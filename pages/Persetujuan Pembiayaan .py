import streamlit as st
from bokeh.models.widgets import Div
import pandas as pd
import numpy as np

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
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #e69138;
    color: white;
    height: 3em;
    width: 17em;
    border-radius:10px;
    border:2px solid #000000;
    font-size:10px;
    font-weight: bold;
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

st.text('Form Pengajuan Pembiayan')
st.button('Download Form')
st.markdown("")
st.markdown("")
st.markdown("")
st.text('Lembar Keputusan Pembiayaan')
with st.expander("Cek Lembar Keputusan Pembiayaan"):
    st.markdown("""
    <iframe src="https://drive.google.com/file/d/1g0IZe4h20idyU1leqjKLhm_0dhEd8Qxy/preview" width="400" height="300" allow="autoplay"></iframe>
    """, unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.markdown("")
st.text('Template Pengajuan Pembiayan')
st.button('Download Template')
st.markdown("")
st.markdown("")
st.markdown("")
st.text('Daftar TBO')
d = {'Emas': ['Doni : NPWP','Didi : NPWP'], 'KPR': ['Anas : KTP','Anis : NPWP'], 'KKB': ['Boni : KTP','Bustomi : KTP']}
df = pd.DataFrame(data=d)
st.table(df)