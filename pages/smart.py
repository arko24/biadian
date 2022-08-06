import streamlit as st
from bokeh.models.widgets import Div

st.set_page_config(page_title='BCAS KONSUMER', page_icon='🖖',layout="wide")

hide_menu = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;} 
        </style>
        """
st.markdown(hide_menu, unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center; color: black;'>SMART-Kit</h2>", unsafe_allow_html=True)
st.markdown("")
st.markdown("")
st.text('1. Handbook Dokumen Pembiayaan')
with open("edoc.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Pdf",
                    data=PDFbyte,
                    file_name="edoc.pdf",
                    mime='application/octet-stream')

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

if st.button('Back'):
    js = "window.location.href = 'http://localhost:8501/main'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)