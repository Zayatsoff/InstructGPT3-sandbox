import streamlit as st
from webapp import web_app
from api.gpt import GPT

GPT_ENGINE = "text-davinci-001"

webapp = web_app(engine=GPT_ENGINE)
number_tokens = web_app.token_box()
temperature = web_app.temp_box()
gpt = GPT(engine=GPT_ENGINE, temperature=temperature, max_tokens=number_tokens)
webapp.run(gpt)
