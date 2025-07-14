import os

from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_and_split_pdfs(pdf_dir):
    docs = []
    for filename in os.listdir(pdf_dir):
        if filename.endswith(".pdf"):
            print(f"Loading: {filename}")
            loader = PyPDFLoader(os.path.join(pdf_dir, filename))
            docs.extend(loader.load())
    splitter = RecursiveCharacterTextSplitter(chunk_size=2500, chunk_overlap=400) #Larger chunk size & overlap for more context
    return splitter.split_documents(docs)

def embed_documents(split_docs):
    print("Embedding documents...")
    embedder = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(split_docs, embedder)
    return vectorstore

def setup_rag_chain(vectorstore):
    llm = OllamaLLM(model="llama3")
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(), #In the future will probably want to manually set k value for optimization
        chain_type="stuff"
    )
    return chain