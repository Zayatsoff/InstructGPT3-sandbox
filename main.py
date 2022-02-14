import streamlit as st
from webapp import web_app
from api import GPT

webapp = web_app()
number_tokens = st.sidebar.slider(
    "Number of Tokens", min_value=5, max_value=2000, value=50
)
gpt = GPT(engine="text-davinci-001", temperature=0.7, max_tokens=number_tokens)
webapp.run(gpt)
