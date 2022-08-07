import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image
image = Image.open('header.png')

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


col1, col2, col3 = st.columns(3)

with col1:
    st.empty()

with col2:
    st.image(image)

with col3:
    st.empty()

st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")


col1, col2, col3, col4, col5=st.columns([0.2, 1, 0.2, 1, 0.2])
with col1:
    st.empty()
with col2:
    st.markdown("<p1 style='text-align: center; color: black;'>PEMBIAYAAN CABANG </p1>", unsafe_allow_html=True)
    option = {
    "legend": {
        "top": 'top'
    },
    "toolbox": {
        "show": "true",
        "feature": {
            "mark": {"show": "true"},
            "dataView": {"show": "true", "readOnly": "false"},
            "restore": {"show": "true"},
            
        }
    },
    "series": [
        {
            "name": 'TOTAL PEMBIAYAAN',
            "type": 'pie',
            "radius": ["30", "120"],
            "center": ['50%', '60%'],
            "roseType": 'area',
            "itemStyle": {
                "borderRadius": "8"
            },
            "data": [
                {"value": 1040, "name": 'JTG'},
                {"value": 948, "name": 'MGD'},
                {"value": 872, "name": 'STR'},
                {"value": 930, "name": 'SMH'},
                {"value": 728, "name": 'KGD'},
                {"value": 726, "name": 'KNR'},
                {"value": 822, "name": 'KGD'},
                {"value": 818, "name": 'BKS'}
            ]
        }
    ],
    "tooltip": {
                    "show": "true"
                },
    "label": {
        "show":"true"
    },
};


    st_echarts(options=option, key="3")
    st.markdown("")
    st.markdown("")
    st.markdown("<p1 style='text-align: center; color: black;'>TARGET </p1>", unsafe_allow_html=True)
    option = {
        "tooltip": {
            "formatter": '{a} <br/>{b} : {c}%'
        },
        "series": [{
            "name": 'Target Tahunan',
            "type": 'gauge',
            "startAngle": 180,
            "endAngle": 0,
            "progress": {
                "show": "true"
            },
            "radius":'100%', 

            "itemStyle": {
                "color": '#0e1dec',
                "shadowColor": 'rgba(0,138,255,0.45)',
                "shadowBlur": 10,
                "shadowOffsetX": 2,
                "shadowOffsetY": 2,
                "radius": '55%',
            },
            "progress": {
                "show": "true",
                "roundCap": "true",
                "width": 15
            },
            "pointer": {
                "length": '60%',
                "width": 8,
                "offsetCenter": [0, '5%']
            },
            "detail": {
                "valueAnimation": "true",
                "formatter": '{value}%',
                "backgroundColor": '#58D9F9',
                "borderColor": '#999',
                "borderWidth": 4,
                "width": '60%',
                "lineHeight": 20,
                "height": 20,
                "borderRadius": 188,
                "offsetCenter": [0, '40%'],
                "valueAnimation": "true",
            },
            "data": [{
                "value": 70.31,
                "name": 'Pencapaian Target Tahunan'
            }]
        }]
    };


    st_echarts(options=option, key="1")


with col3:
    st.empty()

with col4:
    st.markdown("<p1 style='text-align: center; color: black;'>JUMLAH PEMBIAYAAN</p1>", unsafe_allow_html=True)
    option = {
    "tooltip": {
        "trigger": 'item'
    },
    "legend": {
        "top": '5%',
        "left": 'center'
    },
    "series": [
        {
            "name": 'TOTAL PEMBIAYAAN',
            "type": 'pie',
            "radius": ['40%', '75%'],
            "avoidLabelOverlap": "false",
            "itemStyle": {
                "borderRadius": "10",
                "borderColor": '#fff',
                "borderWidth": "2"
            },
            "label": {
                "show": "false",
                "position": 'center'
            },
            "emphasis": {
                "label": {
                    "show": "true",
                    "fontSize": '20',
                    "fontWeight": 'bold'
                }
            },
            "labelLine": {
                "show": "true"
            },
            "data": [
                {"value": 1048, "name": 'EMAS'},
                {"value": 735, "name": 'KPR'},
                {"value": 300, "name": 'KKB'},
            ]
        }
    ]
};

    st_echarts(options=option, key="2")
    st.markdown("")
    st.markdown("")
    st.markdown("<p1 style='text-align: center; color: black;'>PENCAPAIAN BULANAN</p1>", unsafe_allow_html=True)

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
            "data": ['JAN', 'FEB', 'MAR', 'APR', 'MEI', 'JUN', 'JUL']
        },
        "yAxis": {
            "type": 'value'
        },
        "series": [{
            "data": [
                {"value":900, "itemStyle":{"color":"#FF0000"}}, 
                {"value":750, "itemStyle":{"color":"#FF7D00"}},
                {"value":820, "itemStyle":{"color":"#FFFF00"}},
                {"value":650, "itemStyle":{"color":"#00FF00"}},
                {"value":730, "itemStyle":{"color":"#0000FF"}},
                {"value":830, "itemStyle":{"color":"#00FFFF"}},
                {"value":970, "itemStyle":{"color":"#FF00FF"}},
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

with col5:
    st.empty()