import os
from dotenv import load_dotenv
from google import genai

# Carrega o arquivo .env
load_dotenv()

# Pega a chave do Gemini
api_key = os.getenv("GEMINI_API_KEY")

print("1. API KEY encontrada?", bool(api_key))

try:
    # Cria a conexão com o Google Gemini
    client = genai.Client(api_key=api_key)

    print("2. Conexão criada.")

    # Envia uma pergunta simples
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Responda apenas com a palavra funcionando."
    )

    print("3. Gemini respondeu!")
    print("")
    print("RESPOSTA:")
    print(response.text)

except Exception as erro:
    print("")
    print("DEU ERRO:")
    print(type(erro).__name__)
    print(erro)