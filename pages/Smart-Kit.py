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

st.markdown("<h2 style='text-align: center; color: black;'>SMART-Kit</h2>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.text('1. Handbook Dokumen Pembiayaan')

st.markdown("""
<iframe src="https://drive.google.com/file/d/198edwnMUkovWnEQlX51nlmEB7mlDtoxg/preview" width="400" height="300" allow="autoplay"></iframe>
""", unsafe_allow_html=True)
