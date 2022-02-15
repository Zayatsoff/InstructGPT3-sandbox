# imports
import streamlit as st
from config import api_key
import openai

# global vars
API_KEY = api_key

# webapp class
class web_app():
    def __init__(self, engine,description="Description", button_text="Submit", placeholder=""):
        self.btn_txt = button_text
        self.desc = description
        self.set_openai_key(API_KEY)
        self.placeholder = placeholder
        self.engine = engine
        st.markdown(
            """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 250px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 250px;
        margin-left: -250px;
    }
    </style>
    """,
            unsafe_allow_html=True,
        )

    def run(self, gpt):
        st.title("OpenAi's "+ self.engine)
        st.write(" ### Input instructions:")
        self.input = st.text_area(self.placeholder)
        self.button = st.button(self.btn_txt)
        try:
            if self.button:
                st.header("**Result**")
                answer = gpt.submit_request(self.input)
                with st.container():
                    st.markdown(answer["choices"][0]["text"])
        except Exception as e:
            st.success(f"Something Went Wrong! {e}")

    def set_openai_key(self, key):
        # Sets OpenAI key.
        openai.api_key = key
    
    def token_box():
        st.sidebar.number_input(
        "Number of Tokens:", min_value=5, max_value=2000, value=50)
    
    def temp_box():
        st.sidebar.number_input(
        "Temperature:", min_value=0.0, max_value=1.0, value=0.5)
