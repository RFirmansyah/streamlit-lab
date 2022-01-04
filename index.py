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

if 'month' not in st.session_state:
    st.session_state['month'] = 'Jan'
    
df = DataFrame(ds.data_stream(st.session_state['month']))

st.set_page_config(layout="wide")

st.title('DataCo Smart Supply Chain - Dashboard')

with st.container():
    row0_col1, row0_col2, row0_col3, row0_col4, row0_col5 = st.columns(5)
    
    with row0_col1:
        total_item_qty = df['order_item_qty'].sum()
        
        st.header(int(total_item_qty))
        st.markdown('<div style="color: #72b966; font-weight: bold;">Total sales units</div>', unsafe_allow_html=True)
        
    with row0_col2:
        total_inventory_value = round((df['product_price'].sum()*total_item_qty)/1000000,2)
        
        st.header('$'+str(total_inventory_value)+'M')
        st.markdown('<div style="color: #75a1c7; font-weight: bold;">Total item ordered value</div>', unsafe_allow_html=True)
        
    with row0_col3:
        total_sales_value = round((df['sales'].sum())/1000,2)
        
        st.header('$'+str(total_sales_value)+'K')
        st.markdown('<div style="color: #72b966; font-weight: bold;">Total sales value</div>', unsafe_allow_html=True)
        
    with row0_col4:
        total_profit_value = round((df['profit_per_order'].sum())/1000,2)
        
        st.header('$'+str(total_profit_value)+'K')
        st.markdown('<div style="color: #c290b4; font-weight: bold;">Total profit value</div>', unsafe_allow_html=True)
        
    with row0_col5:
        month_option = st.selectbox('Filter month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'), key='fmonth', on_change=ds.update_month)

with st.container():
    row1_col1, row1_col2, row1_col3 = st.columns([1,2,1])

    with row1_col1:
        delivery_status_df = DataFrame(df['delivery_stat'].value_counts())
        delivery_status_df['name'] = delivery_status_df.index
        delivery_status_df['name'] = ds.replace(delivery_status_df['name'],['Late','Advance','On Time','Canceled'])
        delivery_status_df.rename(columns={'delivery_stat':'value'}, inplace=True)
        
        options = vo.set_donut_option(delivery_status_df.to_dict('records'),"Delivery Status | "+st.session_state['month'])
        
        st_echarts(options=options, height="200px")
    
    with row1_col2:
        order_status_df = DataFrame(df['order_stat'].value_counts())
        order_status_df['name'] = order_status_df.index                          
        order_status_df.sort_values(by=['name'], inplace=True)
        
        exclude = ['COMPLETE','CLOSED']
        order_status_df = order_status_df[~order_status_df['name'].isin(exclude)]
        order_status_df['name'] = ds.replace(order_status_df['name'],['Suspected Fraud','Processing','Pending Payment','Pending','Payment Review','On Hold','Canceled'])
        
        options = vo.set_bar_option(list(order_status_df['name']),list(order_status_df['order_stat']),"Order Status | "+st.session_state['month'])
        
        st_echarts(options=options, height="200px")
        
    with row1_col3:
        late_risk_df = DataFrame(df['late_risk'].value_counts())
        late_risk_df['name'] = late_risk_df.index
        late_risk_df['name'] = ds.replace(late_risk_df['name'],['Late','On Time'])
        late_risk_df.rename(columns={'late_risk':'value'}, inplace=True)
        
        options = vo.set_donut_option(late_risk_df.to_dict('records'),"Late Delivery Risk | "+st.session_state['month'])
        
        st_echarts(options=options, height="200px")

with st.container():
    row2_col1, row2_col2, row2_col3 = st.columns(3)        
    
    with row2_col1:
        item_qty_df = DataFrame(df.groupby('order_date_date')['order_item_qty'].sum())
        item_qty_df['name'] = list(range(1,len(item_qty_df)+1))
        
        options = vo.set_line_option(list(item_qty_df['name']),list(item_qty_df['order_item_qty']),"Order Item Quantity Trend | "+st.session_state['month'],"#5470c6")
        
        st_echarts(options=options, height="250px")
        
    with row2_col2:
        sales_df = DataFrame(df.groupby('order_date_date')['sales'].sum())
        sales_df['name'] = list(range(1,len(item_qty_df)+1))
        
        options = vo.set_line_option(list(sales_df['name']),list(sales_df['sales']),"Sales Trend | "+st.session_state['month'],"#91cc75")
        
        st_echarts(options=options, height="250px")
        
    with row2_col3:
        profit_df = DataFrame(df.groupby('order_date_date')['profit_per_order'].sum())
        profit_df['name'] = list(range(1,len(item_qty_df)+1))
        
        options = vo.set_line_option(list(profit_df['name']),list(profit_df['profit_per_order']),"Profit Trend | "+st.session_state['month'],"#73c0de")
        
        st_echarts(options=options, height="250px")

with st.container():
    row3_col1, row3_col2 = st.columns(2)
    
    with row3_col1:
        st.markdown('<div style="text-align: left;">Design by: Rahman Firmansyah</div>', unsafe_allow_html=True)
        
    with row3_col2:
        st.markdown('<div style="text-align: right;">Data source: <a href="https://data.mendeley.com/datasets/8gx2fvg2k6/5">https://data.mendeley.com/datasets/8gx2fvg2k6/5</a></div>', unsafe_allow_html=True)