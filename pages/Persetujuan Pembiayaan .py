import streamlit as st
from bokeh.models.widgets import Div


st.set_page_config(page_title='BCAS KONSUMER', page_icon='🖖',layout="wide")

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


st.text('Form Pengajuan Pembiayan')
st.button('Download')

st.text('Lembar Keputusan Pembiayaan')
with open("edoc.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.markdown("""
<iframe src="https://drive.google.com/file/d/1g0IZe4h20idyU1leqjKLhm_0dhEd8Qxy/preview" width="400" height="300" allow="autoplay"></iframe>
""", unsafe_allow_html=True)


