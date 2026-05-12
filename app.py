import streamlit as st
import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer
from tavily import TavilyClient

# --- 1. CONFIG ---
st.set_page_config(page_title="NorverGPT", page_icon="🤖", layout="wide")
st.markdown("<style>.stApp { background-color: #0b0e11; color: white; }</style>", unsafe_allow_html=True)

TAVILY_API_KEY = "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"

@st.cache_resource
def load_norver_engine():
    model_id = "vikhyatk/moondream2"
    # Added low_cpu_mem_usage and device_map for maximum stability
    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        trust_remote_code=True,
        device_map="auto",
        low_cpu_mem_usage=True
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    return model, tokenizer

# --- 2. MEMORY SYSTEM ---
if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("🤖 NorverGPT")

with st.sidebar:
    st.header("Settings")
    uploaded_image = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    if st.button("🗑️ Reset Memory"):
        st.session_state.messages = []
        st.rerun()

# Display Chat History (Ensures it "remembers")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 3. REASONING ENGINE (The Script & Command Logic) ---
if prompt := st.chat_input("Command NorverGPT..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_area = st.empty()
        # Build context from last 10 turns so it follows past instructions
        history = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages[-10:]])

        try:
            model, tokenizer = load_norver_engine()
            
            if uploaded_image:
                response_area.markdown("⏳ *Analyzing image with context...*")
                image = Image.open(uploaded_image).convert("RGB")
                instruction = f"History: {history}\n\nTask: {prompt}"
                final_output = model.answer_question(model.encode_image(image), instruction, tokenizer)
            else:
                response_area.markdown("🌐 *Searching & Reasoning...*")
                tavily = TavilyClient(api_key=TAVILY_API_KEY)
                search = tavily.search(query=prompt, search_depth="advanced")
                web_data = "\n".join([r['content'] for r in search['results']])
                
                # Full instruction injection for code generation and memory
                final_instruction = f"System: Use history and web data. If code is asked, write code. History: {history}\n\nWeb Data: {web_data}\n\nCommand: {prompt}"
                final_output = model.answer_question(None, final_instruction, tokenizer)
            
            response_area.markdown(final_output)
            st.session_state.messages.append({"role": "assistant", "content": final_output})
        except Exception as e:
            response_area.error(f"Error: {e}")
