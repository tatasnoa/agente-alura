# Agente Inteligente de Documentos com RAG

Projeto desenvolvido para o **Challenge Alura - Agente Inteligente**, com o objetivo de criar uma aplicação capaz de ler documentos em PDF e responder perguntas com base no conteúdo enviado pelo usuário.

A aplicação utiliza uma arquitetura **RAG (Retrieval-Augmented Generation)**, combinando busca semântica em documentos com um modelo de inteligência artificial generativa.

## Funcionalidades

* Upload de arquivos PDF
* Extração automática do texto do documento
* Divisão do conteúdo em pequenos trechos
* Criação de embeddings para busca semântica
* Armazenamento dos vetores com FAISS
* Recuperação dos trechos mais relevantes para cada pergunta
* Geração de respostas utilizando o Google Gemini
* Interface web criada com Streamlit

## Arquitetura da solução

O fluxo da aplicação funciona da seguinte forma:

```text
Usuário envia um PDF
        ↓
PyPDF extrai o texto
        ↓
RecursiveCharacterTextSplitter
divide o texto em chunks
        ↓
HuggingFace Embeddings
transforma os textos em vetores
        ↓
FAISS
armazena e realiza a busca semântica
        ↓
Retriever
seleciona os trechos mais relevantes
        ↓
LangChain
envia o contexto + pergunta
        ↓
Google Gemini
gera a resposta
        ↓
Streamlit
exibe a resposta ao usuário
```

Essa abordagem permite que o modelo utilize informações encontradas no próprio documento para responder às perguntas.

## Tecnologias utilizadas

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **HuggingFace Embeddings**
* **Sentence Transformers**
* **FAISS**
* **PyPDF**
* **Python Dotenv**

O modelo utilizado para geração das respostas é:

```text
gemini-3.6-flash
```

Para os embeddings foi utilizado:

```text
all-MiniLM-L6-v2
```

Os embeddings são executados localmente.

## Estrutura do projeto

```text
agente-alura/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── teste_gemini.py
```

O arquivo `.env`, que contém a chave da API do Gemini, não é enviado ao GitHub por questões de segurança.

## Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/tatasnoa/agente-alura.git
```

Entre na pasta do projeto:

```bash
cd agente-alura
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Configure a chave da API

Crie um arquivo chamado:

```text
.env
```

Dentro dele, adicione:

```text
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

Substitua `SUA_CHAVE_AQUI` pela sua chave da API do Google Gemini.

### 4. Execute a aplicação

```bash
streamlit run app.py
```

Após executar o comando, o Streamlit abrirá a aplicação no navegador.

## Como utilizar

1. Abra a aplicação.
2. Faça upload de um arquivo PDF.
3. Aguarde o processamento do documento.
4. Digite uma pergunta relacionada ao conteúdo.
5. O agente buscará os trechos mais relevantes e utilizará essas informações para gerar uma resposta.

## Exemplos de perguntas

Dependendo do documento enviado, o usuário pode perguntar:

```text
Qual é o assunto principal deste documento?
```

```text
Quais são os principais pontos apresentados no texto?
```

```text
Segundo o documento, quais são as conclusões apresentadas?
```

```text
Explique de forma resumida o conteúdo deste documento.
```

## Exemplo de resposta

Pergunta:

```text
Qual é o assunto principal deste documento?
```

Exemplo de resposta gerada pelo agente:

```text
O documento apresenta como tema principal os conceitos abordados no material enviado, destacando os pontos mais relevantes encontrados no texto.
```

As respostas podem variar de acordo com o conteúdo do PDF utilizado.

## RAG - Retrieval-Augmented Generation

A aplicação utiliza RAG para melhorar a qualidade das respostas.

Em vez de enviar todo o documento diretamente ao modelo de inteligência artificial, o sistema:

1. Divide o documento em pequenos trechos.
2. Transforma os trechos em representações vetoriais.
3. Busca os trechos semanticamente mais próximos da pergunta.
4. Envia somente o contexto relevante para o modelo Gemini.
5. Gera uma resposta baseada nesse contexto.

Isso permite trabalhar de maneira mais eficiente com documentos maiores.

## Deploy na Oracle Cloud Infrastructure

A aplicação está publicada utilizando a Oracle Cloud Infrastructure (OCI).

### Link da aplicação

http://140.238.180.167:8501

### Evidência do deploy

A aplicação foi publicada na Oracle Cloud Infrastructure (OCI) e está disponível publicamente por meio do link acima. O deploy foi validado com o envio e processamento de um documento PDF e a realização de perguntas sobre seu conteúdo.

## Segurança

A chave da API do Google Gemini é armazenada no arquivo `.env`.

Esse arquivo está incluído no `.gitignore` para impedir que credenciais sejam publicadas no GitHub.

Nunca compartilhe ou envie chaves de API diretamente para repositórios públicos.

## Challenge Alura

Este projeto foi desenvolvido como parte do **Challenge Alura - Agente Inteligente**, atendendo aos requisitos de:

* repositório público no GitHub;
* histórico de commits;
* documentação do projeto;
* agente inteligente funcional;
* leitura e processamento de documentos;
* aplicação de inteligência artificial;
* deploy na OCI;
* evidência da aplicação em funcionamento.
