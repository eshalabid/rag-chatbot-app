import streamlit as st
import requests

st.title("📚 RAG Chatbot")
st.write("Ask whatever you want :)")
query = st.text_input("Ask your question:")

if st.button("Submit") and query:
    with st.spinner("Thinking..."):
        response = requests.post("http://127.0.0.1:8000/api/chatbot/rag", json={"query": query})
        if response.status_code == 200:
            st.success(response.json()["answer"])
        else:
            st.error("Something went wrong. Please check the server.")
