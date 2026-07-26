import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from config import (
    PDF_PATH, CHROMA_PERSIST_DIR, CHUNK_SIZE, 
    CHUNK_OVERLAP, OLLAMA_EMBEDDING_MODEL, OLLAMA_BASE_URL
)

def create_vector_store(force_rebuild=False):
    """
    Loads PDF, splits it, creates embeddings using Ollama, and stores in ChromaDB.
    """
    os.makedirs(os.path.dirname(CHROMA_PERSIST_DIR), exist_ok=True)
    
    # Check if vector store exists and we don't want to rebuild
    if os.path.exists(CHROMA_PERSIST_DIR) and not force_rebuild:
        print(f"Loading existing vector store from {CHROMA_PERSIST_DIR}")
        embedding = OllamaEmbeddings(
            model=OLLAMA_EMBEDDING_MODEL,
            base_url=OLLAMA_BASE_URL
        )
        return Chroma(persist_directory=CHROMA_PERSIST_DIR, embedding_function=embedding)
    
    # Check if PDF exists
    if not os.path.exists(PDF_PATH):
        raise FileNotFoundError(f"PDF not found at {PDF_PATH}. Please add the file.")
    
    print(f"Loading and processing PDF: {PDF_PATH}")
    
    # Load PDF
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    
    if not documents:
        raise ValueError("No text could be extracted from the PDF.")
    
    print(f"Loaded {len(documents)} pages from PDF")
    
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    docs = text_splitter.split_documents(documents)
    
    print(f"Split into {len(docs)} chunks")
    
    # Create embeddings using Ollama
    embedding = OllamaEmbeddings(
        model=OLLAMA_EMBEDDING_MODEL,
        base_url=OLLAMA_BASE_URL
    )
    
    # Store in ChromaDB
    print(f"Creating vector store at {CHROMA_PERSIST_DIR}")
    vector_store = Chroma.from_documents(
        docs, 
        embedding, 
        persist_directory=CHROMA_PERSIST_DIR
    )
    vector_store.persist()
    
    print("Vector store created successfully!")
    return vector_store