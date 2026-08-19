import streamlit as st
import os
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Carrega a chave do arquivo .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Agente de Documentos - Alura", page_icon="🤖")
st.title("🤖 Agente Inteligente de Documentos")
st.write("Envie um PDF e faça perguntas sobre o conteúdo dele!")

# 1. Upload do documento PDF
uploaded_file = st.file_uploader("Envie seu arquivo PDF aqui", type="pdf")

if uploaded_file is not None:
    with st.spinner("Lendo e processando o documento..."):
        # Extrair texto do PDF
        pdf_reader = PdfReader(uploaded_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""

        # Dividir o texto em pedaços (chunks)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = text_splitter.split_text(text)

        # Usando embeddings locais e gratuitos
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
        retriever = vectorstore.as_retriever()

        # Configurar a IA do Gemini
        llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash", google_api_key=api_key, temperature=0)
        
        system_prompt = (
            "Você é um assistente encarregado de responder a dúvidas com base no documento fornecido.\n"
            "Se não souber a resposta, diga que não encontrou no documento.\n\n"
            "Contexto:\n{context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])

        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)

        st.success("Documento processado com sucesso!")

    # 2. Campo para o usuário fazer a pergunta
    user_question = st.text_input("Qual é a sua dúvida sobre esse documento?")

    if user_question:
        with st.spinner("Pensando na resposta..."):
            response = rag_chain.invoke({"input": user_question})
            st.subheader("Resposta do Agente:")
            st.write(response["answer"])