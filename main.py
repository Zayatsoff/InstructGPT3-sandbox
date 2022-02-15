import streamlit as st
from webapp import web_app
from api.gpt import GPT

# pick engine
GPT_ENGINE = "text-davinci-001"

# assign webapp
webapp = web_app(engine=GPT_ENGINE)

# create token and temperatre box
number_tokens = web_app.token_box()
print(number_tokens)
temperature = web_app.temp_box()

# assign gpt
gpt = GPT(engine=GPT_ENGINE, temperature=temperature, max_tokens=number_tokens)

# run
webapp.run(gpt)
