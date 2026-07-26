import streamlit as st
import os
import time
from config import OLLAMA_MODEL, OLLAMA_EMBEDDING_MODEL
from pdf_loader import create_vector_store
from rag_chain import get_rag_chain, get_ollama_status
from syllabus import get_lesson, DAILY_LESSONS

CHAIN_VERSION = 2

# Page config
st.set_page_config(
    page_title="AI ML Teacher - Learn Machine Learning",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #FF6B6B;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        margin-bottom: 2rem;
    }
    .lesson-card {
        background-color: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #FF6B6B;
        margin-bottom: 1rem;
    }
    .task-box {
        background-color: #e8f4fd;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #cce5ff;
        margin-top: 1rem;
    }
    .status-ok {
        color: #28a745;
        font-weight: 600;
    }
    .status-error {
        color: #dc3545;
        font-weight: 600;
    }
    .stChatInput textarea {
        border-radius: 20px !important;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "chain" not in st.session_state:
    st.session_state.chain = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "current_day" not in st.session_state:
    st.session_state.current_day = 1
if "vector_store_ready" not in st.session_state:
    st.session_state.vector_store_ready = False
if "initialized" not in st.session_state:
    st.session_state.initialized = False
if st.session_state.get("chain_version") != CHAIN_VERSION:
    st.session_state.initialized = False
    st.session_state.chain = None
    st.session_state.chain_version = CHAIN_VERSION

# Sidebar
with st.sidebar:
    st.markdown("## 🤖 AI ML Teacher")
    st.markdown("---")
    
    # Status indicator
    st.markdown("### System Status")
    
    if not st.session_state.initialized:
        status = get_ollama_status()
        
        if status["running"]:
            st.markdown("✅ **Ollama:** Running")
            
            if status["has_llm"]:
                st.markdown(f"✅ **LLM:** {status.get('models', ['Not found'])[0] if status.get('models') else 'Ready'}")
            else:
                st.markdown(f"❌ **LLM Model Missing:** Run `ollama pull {OLLAMA_MODEL}`")
                
            if status["has_embeddings"]:
                st.markdown(f"✅ **Embeddings:** Ready")
            else:
                st.markdown(f"❌ **Embeddings Model Missing:** Run `ollama pull {OLLAMA_EMBEDDING_MODEL}`")
        else:
            st.markdown("❌ **Ollama:** Not running")
            st.markdown("Please start Ollama: `ollama serve`")
    
    st.markdown("---")
    
    # Syllabus navigation
    st.markdown("## 📚 Syllabus")
    st.markdown("Select a day to see today's lesson:")
    
    selected_day = st.selectbox(
        "Day",
        options=[d["day"] for d in DAILY_LESSONS],
        format_func=lambda x: f"Day {x}: {get_lesson(x)['topic']}" if get_lesson(x) else f"Day {x}",
        index=st.session_state.current_day - 1,
        key="day_selector"
    )
    
    if st.button("📖 Load Today's Lesson", use_container_width=True):
        st.session_state.current_day = selected_day
        st.session_state.messages = []
        st.rerun()
    
    # Current lesson display
    st.markdown("---")
    lesson = get_lesson(st.session_state.current_day)
    if lesson:
        st.markdown(f"### 📖 Day {lesson['day']}: {lesson['topic']}")
        st.markdown(f"**Description:** {lesson['description']}")
        
        st.markdown("**Learning Objectives:**")
        for obj in lesson.get("learning_objectives", []):
            st.markdown(f"- {obj}")
        
        st.markdown("---")
        st.markdown("### 🎯 Today's Task")
        st.markdown(f"_{lesson['task']}_")
    
    st.markdown("---")
    st.markdown("### 📖 About This Teacher")
    st.markdown("""
    This AI Teacher is powered by:
    - **Ollama** for local LLM
    - **LangChain** for RAG
    - **Machine Learning with Python Cookbook** as knowledge base
    
    All processing is done locally. No data is sent to the cloud.
    """)

# Main chat interface
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<p class="main-header">💬 Ask Your ML Questions</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Your AI teacher is here to help you learn!</p>', unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


def build_chat_history(messages):
    """Convert Streamlit message dicts into chat history pairs for LangChain."""
    chat_history = []
    last_user_message = None

    for message in messages:
        if message["role"] == "user":
            last_user_message = message["content"]
        elif message["role"] == "assistant" and last_user_message is not None:
            chat_history.append((last_user_message, message["content"]))
            last_user_message = None

    return chat_history

# Initialize chain on first message
def initialize_rag():
    """Initialize the RAG chain with progress updates"""
    with st.status("Initializing AI Teacher...", expanded=True) as status:
        status.write("📄 Loading and processing the ML Cookbook...")
        try:
            vector_store = create_vector_store()
            st.session_state.vector_store_ready = True
        except FileNotFoundError:
            st.error(f"PDF not found at the specified path. Please add the file.")
            st.stop()
        except Exception as e:
            st.error(f"Error loading PDF: {e}")
            st.stop()
        
        status.write("🤖 Creating RAG chain with Ollama...")
        st.session_state.chain = get_rag_chain(vector_store)
        st.session_state.initialized = True
        
        status.write("✅ Ready! You can now ask questions.")
        status.update(label="Ready!", state="complete")
        time.sleep(1)

# Chat input
if prompt := st.chat_input("Ask me anything about machine learning..."):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Initialize if not done
    if not st.session_state.initialized:
        initialize_rag()
    
    # Generate response
    if st.session_state.chain:
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Add lesson context
                    lesson = get_lesson(st.session_state.current_day)
                    day_context = f"The student is on Day {lesson['day']}: {lesson['topic']}. "
                    full_prompt = f"{day_context}\n\nStudent question: {prompt}"
                    chat_history = build_chat_history(st.session_state.messages[:-1])
                    
                    # Get response
                    response = st.session_state.chain.invoke({
                        "question": full_prompt,
                        "chat_history": chat_history,
                    })
                    answer = response["answer"]
                    
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                    
                    # Show source documents (optional)
                    if response.get("source_documents"):
                        with st.expander("📚 Sources from the book"):
                            for doc in response["source_documents"][:3]:
                                st.caption(doc.page_content[:300] + "...")
                                st.divider()
                except Exception as e:
                    st.error(f"Error: {e}")
                    st.info("Make sure Ollama is running and models are downloaded.")

# Footer
st.markdown("---")
st.caption("🤖 AI ML Teacher | Powered by Ollama & LangChain | All processing is local and private")
