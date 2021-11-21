import streamlit as st
import pandas as pd
from pandas import DataFrame
import numpy as np
from st_aggrid import AgGrid
from gsheetsdb import connect
from streamlit_echarts import st_echarts

st.set_page_config(layout="wide")

with st.container():
    row1_col1, row1_col2, row1_col3 = st.columns([1,2,1])
    
    with row1_col1:
        conn = connect()
        result = conn.execute("""
            SELECT
                COUNT("Delivery Status") as value,
                "Delivery Status" AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA'            
            GROUP BY
                "Delivery Status"
        """, headers=1)
        
        df = DataFrame(result)
        
        options = {
            "color": ["#7dc370", "#ffbeb2", "#fa8f79", "#b3e0a6"],
            "tooltip": {"trigger": "item"},
            #"legend": {"top": "5%", "left": "center"},
            "series": [
                {
                    "name": "Delivery Status",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "avoidLabelOverlap": False,
                    "itemStyle": {
                        "borderRadius": 5,
                        "borderColor": "#fff",
                        "borderWidth": 2,
                    },
                    "label": {"show": False, "position": "center"},
                    "emphasis": {
                        "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                    },
                    "labelLine": {"show": False},
                    "data": df.to_dict('records'),
                }
            ],
        }
        
        st_echarts(
            options=options, height="200px"
        )
        
    with row1_col2:
        conn = connect()
        result = conn.execute("""
            SELECT
                COUNT("Order Status") as value,
                "Order Status" AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA' AND      
                "Order Status" <> 'COMPLETE' AND
                "Order Status" <> 'CLOSED'    
            GROUP BY
                "Order Status"
        """, headers=1)
        
        df = DataFrame(result)
        
        options = {
          "title": {
            "text": "Status Order"
          },
          "color": ["#d3293d", "#da323f", "#ae123a", "#fb9984", "#f36754", "#fa8f79", "#f05c4d"],
          "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
              "type": "shadow"
            }
          },
          "legend": {},
          "grid": {
            "left": "3%",
            "right": "4%",
            "bottom": "3%",
            "containLabel": True
          },
          "xAxis": {
            "type": "value",
            "boundaryGap": ["0", "0.01"]
          },
          "yAxis": {
            "type": "category",
            "data": list(df['name'])
          },
          "series": [
            {
              #"name": "2011",
              "type": "bar",
              "data": list(df['value'])
            }
          ]
        }
        
        st_echarts(
            options=options, height="200px"
        )                                      
    
    with row1_col3:
        conn = connect()
        result = conn.execute("""
            SELECT
                COUNT(Late_delivery_risk) as value,
                Late_delivery_risk AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA'            
            GROUP BY
                Late_delivery_risk
        """, headers=1)
        
        df = DataFrame(result)
        
        nameList = list()
        
        for i in df['name']:
            if i == 0:
              nameList.append('Not Late')
            else:
              nameList.append('Late')
              
        df['name'] = nameList
        
        options = {
            "color": ["#7dc370", "#ffbeb2", "#fa8f79", "#b3e0a6"],
            "tooltip": {"trigger": "item"},
            #"legend": {"top": "5%", "left": "center"},
            "series": [
                {
                    "name": "Delivery Status",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "avoidLabelOverlap": False,
                    "itemStyle": {
                        "borderRadius": 5,
                        "borderColor": "#fff",
                        "borderWidth": 2,
                    },
                    "label": {"show": False, "position": "center"},
                    "emphasis": {
                        "label": {"show": True, "fontSize": "40", "fontWeight": "bold"}
                    },
                    "labelLine": {"show": False},
                    "data": df.to_dict('records'),
                }
            ],
        }
        
        st_echarts(
            options=options, height="200px"
        )                  

with st.container():
    row2_col1, row2_col2, row2_col3 = st.columns(3)
    
    with row2_col1:
        conn = connect()
        result = conn.execute("""
            SELECT
                SUM("Order Item Quantity") AS value,
                "Order Date Part" AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA' AND
                "Order Month" = 'Nov'
            GROUP BY
                "Order Month", "Order Date Part"
            ORDER BY
                "Order Date Part"   
        """, headers=1)
        
        df = DataFrame(result)
        df['value'] = round(df['value'])
        
        options = {
          "xAxis": {
            "type": "category",
            "data": list(df['name'])
          },
          "yAxis": {
            "type": "value"
          },
          "series": [
            {
              "data": list(df['value']),
              "type": "line",
              "smooth": True,
              "label": { "position": "top" }
            }
          ]
        }
        
        st_echarts(
            options=options, height="300px",
        )
    
    with row2_col2:
        conn = connect()
        result = conn.execute("""
            SELECT
                SUM("Sales") AS value,
                "Order Date Part" AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA' AND
                "Order Month" = 'Nov'
            GROUP BY
                "Order Month", "Order Date Part"
            ORDER BY
                "Order Date Part"   
        """, headers=1)
        
        df = DataFrame(result)
        df['value'] = round(df['value'])
        
        options = {
          "xAxis": {
            "type": "category",
            "data": list(df['name'])
          },
          "yAxis": {
            "type": "value"
          },
          "series": [
            {
              "data": list(df['value']),
              "type": "line",
              "smooth": True,
              "label": { "position": "top" }
            }
          ]
        }
        
        st_echarts(
            options=options, height="300px",
        )
    
    with row2_col3:
        conn = connect()
        result = conn.execute("""
            SELECT
                SUM("Order Profit Per Order") AS value,
                "Order Date Part" AS name
            FROM
                "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"         
            WHERE
                "Customer State" = 'CA' AND
                "Order Month" = 'Nov'
            GROUP BY
                "Order Month", "Order Date Part"
            ORDER BY
                "Order Date Part"   
        """, headers=1)
        
        df = DataFrame(result)
        df['value'] = round(df['value'])
        
        options = {
          "xAxis": {
            "type": "category",
            "data": list(df['name'])
          },
          "yAxis": {
            "type": "value"
          },
          "series": [
            {
              "data": list(df['value']),
              "type": "line",
              "smooth": True,
              "label": { "position": "top" }
            }
          ]
        }
        
        st_echarts(
            options=options, height="300px",
        )                         