import streamlit as st
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

try:
    model = load_model()
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}")
