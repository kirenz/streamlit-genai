import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜🔗 Langchain - Blog Outline Generator App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
#openai_api_key = os.getenv('OPENAI_API_KEY')

def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="gpt-4o", openai_api_key=openai_api_key)
    # Prompt
    template = "As an experienced content marketing expert, generate an outline for a blog about {topic}."
    prompt = PromptTemplate(input_variables=["topic"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm.invoke(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)