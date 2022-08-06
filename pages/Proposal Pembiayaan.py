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

st.text('Input Data Nasabah Pembiayaan')
title = st.text_input('Nama Nasabah', '')
title = st.text_input('Nik Nasabah', '')
title = st.text_input('Alamat', '')
title = st.text_input('No Telpon', '')
option = st.selectbox(
     'Pengajuan Pembiayan',
     ('Emas', 'KKB', 'KPR'))

st.write('Pilihan Pembiayaan:', option)

uploaded_files = st.file_uploader("Chose File", accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
     st.write(bytes_data)
