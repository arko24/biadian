import streamlit as st
import streamlit.components.v1 as components
from bokeh.models.widgets import Div

st.set_page_config(page_title='BCAS KONSUMER',layout="wide")

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

st.set_page_config(layout="wide")

st.markdown("<h2 style='text-align: center; color: black;'>Log In </h2>", unsafe_allow_html=True)
hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)
st.markdown("***")
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #e69138;
    color: white;
    height: 2em;
    width: 6em;
    border-radius:10px;
    border:2px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background-color:#e69138;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)

title = st.text_input('Email')
title = st.text_input('Password')
st.markdown("")

if st.button('Log In'):
    js = "window.location.href = 'https://biadian.herokuapp.com/main'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

st.markdown("***")


    
