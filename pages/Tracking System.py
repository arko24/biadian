import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(page_title='BCAS KONSUMER', layout="wide")

def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp{{
            background-image: url(https://github.com/arko24/biadian.github.io/blob/main/main.jpg?raw=true);
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()

hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer,header {visibility: hidden;} 
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)

image = Image.open('KPR.jpeg')
st.image(image, width=300,)
