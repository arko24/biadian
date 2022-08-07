import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

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

st.markdown("<h2 style='text-align: center; color: black;'>Q & A</h2>", unsafe_allow_html=True)

df = pd.read_excel("Q&A Pembiayaan.xlsx")
st.table(df)