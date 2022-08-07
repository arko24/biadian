import streamlit as st
import streamlit.components.v1 as components
from requests_html import HTMLSession
import webbrowser
import urllib.request


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


get_url= webbrowser.open('https://www.appsheet.com/start/7f4ea332-81b3-45bf-9091-385a5d99cec7')
st.markdown(get_url)