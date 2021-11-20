import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit_echarts'])

import streamlit as st
import pandas as pd
from pandas import DataFrame
import numpy as np
from streamlit_echarts import st_echarts

import datastream as ds
import vizopt as vo

df = DataFrame(ds.data_stream())

st.set_page_config(layout="wide")

with st.container():
    row1_col1, row1_col2, row1_col3 = st.columns([1,2,1])

    with row1_col1:
        delivery_status_df = DataFrame(df['delivery_stat'].value_counts())
        delivery_status_df['name'] = delivery_status_df.index
        delivery_status_df.rename(columns={'delivery_stat':'value'}, inplace=True)
        
        options = vo.set_donut_option(delivery_status_df.to_dict('records'))
        
        st_echarts(options=options, height="200px")
    
    with row1_col2:
        order_status_df = DataFrame(df['order_stat'].value_counts())
        order_status_df['name'] = order_status_df.index                          
        order_status_df.sort_values(by=['name'], inplace=True)
        
        exclude = ['COMPLETE','CLOSED']
        order_status_df = order_status_df[~order_status_df['name'].isin(exclude)]
        
        options = vo.set_bar_option(list(order_status_df['name']),list(order_status_df['order_stat']))
        
        st_echarts(options=options, height="200px")
        
    with row1_col3:
        late_risk_df = DataFrame(df['late_risk'].value_counts())
        late_risk_df['name'] = late_risk_df.index
        late_risk_df.rename(columns={'late_risk':'value'}, inplace=True)
        
        nameList = list()
        
        for i in late_risk_df['name']:
            if i == 0:
              nameList.append('Not Late')
            else:
              nameList.append('Late')
              
        late_risk_df['name'] = nameList
        
        options = vo.set_donut_option(late_risk_df.to_dict('records'))
        
        st_echarts(options=options, height="200px")

with st.container():
    row2_col1, row2_col2, row2_col3 = st.columns(3)        
    
    with row2_col1:
        item_qty_df = DataFrame(df.groupby('order_date_date')['order_item_qty'].sum())
        item_qty_df['name'] = list(range(1,31))
        
        options = vo.set_line_option(list(item_qty_df['name']),list(item_qty_df['order_item_qty']))
        
        st_echarts(options=options, height="250px")
        
    with row2_col2:
        sales_df = DataFrame(df.groupby('order_date_date')['sales'].sum())
        sales_df['name'] = list(range(1,31))
        
        options = vo.set_line_option(list(sales_df['name']),list(sales_df['sales']))
        
        st_echarts(options=options, height="250px")
        
    with row2_col3:
        profit_df = DataFrame(df.groupby('order_date_date')['profit_per_order'].sum())
        profit_df['name'] = list(range(1,31))
        
        options = vo.set_line_option(list(profit_df['name']),list(profit_df['profit_per_order']))
        
        st_echarts(options=options, height="250px")