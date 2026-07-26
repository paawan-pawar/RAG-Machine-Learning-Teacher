from langchain_community.llms import Ollama
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_classic.prompts import PromptTemplate
from config import OLLAMA_MODEL, OLLAMA_EMBEDDING_MODEL, OLLAMA_BASE_URL, TEMPERATURE, TOP_K_RETRIEVAL

# Custom prompt template
TEACHER_PROMPT_TEMPLATE = """
You are an AI Machine Learning Teacher named "ML Tutor". You are teaching a student based on the book "Machine Learning with Python Cookbook".

Your personality:
- Patient and encouraging
- Clear and concise in explanations
- Use analogies when helpful
- Encourage hands-on practice

Your response guidelines:
1. Use the provided context from the textbook to answer the student's question
2. If the context doesn't contain the answer, use your own ML knowledge but mention it
3. Provide code examples when relevant
4. Keep explanations clear and educational

Context from textbook:
{context}

Chat history:
{chat_history}

Student's question: {question}

Teacher's response (be clear, educational, and encouraging):
"""

def create_prompt_template():
    """Create the prompt template for the RAG chain"""
    return PromptTemplate(
        template=TEACHER_PROMPT_TEMPLATE,
        input_variables=["context", "chat_history", "question"]
    )

def get_rag_chain(vector_store):
    """Creates and returns a conversational RAG chain using Ollama"""
    
    # Initialize Ollama LLM
    llm = Ollama(
        model=OLLAMA_MODEL,
        base_url=OLLAMA_BASE_URL,
        temperature=TEMPERATURE,
        top_k=40,
        top_p=0.9,
        num_predict=2048,
    )
    
    # Create prompt template
    prompt = create_prompt_template()
    
    # Build the chain
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": TOP_K_RETRIEVAL}),
        combine_docs_chain_kwargs={"prompt": prompt},
        return_source_documents=True,
        verbose=False
    )
    
    return chain

def get_ollama_status():
    """Check if Ollama is running and has the required models"""
    import requests
    try:
        # Check if Ollama is running
        response = requests.get(f"{OLLAMA_BASE_URL}/api/tags")
        if response.status_code == 200:
            models = response.json().get("models", [])
            model_names = [m.get("name", "") for m in models]
            
            # Check for required models
            has_llm = any(OLLAMA_MODEL in name for name in model_names)
            has_embeddings = any(OLLAMA_EMBEDDING_MODEL in name for name in model_names)
            
            return {
                "running": True,
                "models": model_names,
                "has_llm": has_llm,
                "has_embeddings": has_embeddings,
                "missing_models": []
            }
        else:
            return {"running": False, "error": f"Status code: {response.status_code}"}
    except Exception as e:
        return {"running": False, "error": str(e)}