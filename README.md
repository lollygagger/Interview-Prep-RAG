# Interview Prep Assistant (Local RAG Chatbot)

This is a lightweight Retrieval-Augmented Generation (RAG) chatbot that runs **entirely locally** using your interview prep PDFs. It uses a vector database + local LLM (via [Ollama](https://ollama.com)) to answer questions about interview material.

---

## Features

- Local PDF ingestion
- Text chunking & semantic search (FAISS + Sentence Transformers)
- Answers questions using a local LLM like `llama3` or `mistral` via Ollama
- CLI interface


## Built With
- **LangChain** v0.2+
- **LangChain Community** for Ollama, FAISS, HuggingFace
- **FAISS** for local vector search
- **Sentence Transformers** (`all-MiniLM-L6-v2`) for embeddings
- **Ollama** for running LLMs locally
- **PyPDF** for parsing PDFs

---

## Installation

1. **Clone the project** or download the files:

    ```bash
    git clone https://github.com/lollygagger/interview-prep-rag.git
    cd interview-prep-rag
    ```

2. **(Optional)** Create a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate  # Windows
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

---

## Running the Chatbot

```bash
python main.py
```

---

## Setup Ollama

Make sure [Ollama](https://ollama.com) is installed and running:

```bash
ollama run llama3