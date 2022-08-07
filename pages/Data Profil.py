from streamlit_echarts import st_echarts
import streamlit as st
from PIL import Image

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

image = Image.open('user.jpeg')
st.image(image, width=100,)

st.text('Data AO')
st.text('Nama    : DIAN RISDIANA')
st.text('Cabang  : JATINEGARA')

st.markdown("")
st.markdown("")

st.text('KEY PERFORMA INDICATOR')
option = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":920, "itemStyle":{"color":"#FF0000"}}, 
                {"value":700, "itemStyle":{"color":"#FF7D00"}},
                {"value":1000, "itemStyle":{"color":"#FFFF00"}},
                {"value":950, "itemStyle":{"color":"#00FF00"}},
                {"value":760, "itemStyle":{"color":"#0000FF"}},
                {"value":730, "itemStyle":{"color":"#00FFFF"}},
                {"value":1020, "itemStyle":{"color":"#FF00FF"}},
                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        };
st_echarts(options=option, key="1")


st.text('PENCAPAIAN')
option = {
        "toolbox": {
        "show": "true",
        "feature": {
          "dataZoom": {
            "yAxisIndex": "none"
          },
          "dataView": {
            "readOnly": "false"
          },
          "magicType": {
            "type": ["line", "bar"]
          },
          "restore": {"show":"true"},
        }
      },
        "xAxis": {
            "type": 'category',
            "data": ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":900, "itemStyle":{"color":"#FF0000"}}, 
                {"value":750, "itemStyle":{"color":"#FF7D00"}},
                {"value":1020, "itemStyle":{"color":"#FFFF00"}},
                {"value":850, "itemStyle":{"color":"#00FF00"}},
                {"value":560, "itemStyle":{"color":"#0000FF"}},
                {"value":930, "itemStyle":{"color":"#00FFFF"}},
                {"value":1070, "itemStyle":{"color":"#FF00FF"}},
                ],
            "type": 'bar'

        }],
        "tooltip": {
                        "show": "true"
                    },
        "label": {
            "show":"true"
        },
        
                        
        };
st_echarts(options=option, key="4")
