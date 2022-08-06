import streamlit as st
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

hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer,header {visibility: hidden;}
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

if st.button('Data Profil'):
    js = "window.location.href = 'https://biadian.herokuapp.com/profil '"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

st.button('Tracking System')

if st.button('SMART-Kit'):
    js = "window.location.href = 'https://biadian.herokuapp.com/smart '"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

st.button('Proposal Pembiayaan')
st.button('Persetujuan Pembiayaan')
st.button('eDocument')

if st.button('Sign Out'):
    js = "window.location.href = 'https://biadian.herokuapp.com/ '"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)
    
