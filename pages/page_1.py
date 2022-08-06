import streamlit as st
from bokeh.models.widgets import Div


st.set_page_config(
    initial_sidebar_state="collapsed",
    layout="centered")

hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;} 
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #9fc5e8;
    color: white;
    height: 2em;
    width: 16em;
    border-radius:10px;
    border:2px solid #000000;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background-color:#9fc5e8;
}

div.stButton > button:active {
	position:relative;
	top:3px;
    
}

</style>""", unsafe_allow_html=True)

st.button('Data Profil')
st.button('Tracking System')
st.button('SMART-Kit')
st.button('Proposal Pembiayaan')
st.button('Persetujuan Pembiayaan')
st.button('eDocument')

if st.button('Sign Out'):
    js = "window.location.href = 'http://localhost:8501'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
    