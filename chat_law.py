import streamlit as st
from langchain_openai import ChatOpenAI

st.title("🦜🔗 ChatLaw")
st.caption("🚀 Search accurate law related information by chating with LLM")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"


def generate_response(input_text):
    llm = ChatOpenAI(openai_api_key=openai_api_key)
    response = llm.invoke(input_text)
    st.info(response.content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:", "What are 3 key advice for learning how to code?"
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        generate_response(text)
