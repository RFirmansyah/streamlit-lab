import sys
import subprocess

#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gsheetsdb'])

import streamlit as st
from gsheetsdb import connect

source = "https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/"

template = """
        SELECT
            "Delivery Status" AS delivery_stat,
            "Order Status" AS order_stat,
            Late_delivery_risk AS late_risk,        
            "Order Date Part" AS order_date_date,
            "Order Item Quantity" AS order_item_qty,
            "Sales" AS sales,
            "Order Profit Per Order" AS profit_per_order,
            "Order Item Product Price" AS product_price
        FROM
            "{0}"                     
        WHERE
            "Customer State" = 'CA' AND
            "Order Month" = '{1}'
    """

def data_stream(month):
    query = template.format(source,month)
    
    conn = connect()
    result = conn.execute(query, headers=1)
    
    return result
    
def replace(names,replacement):
    nameList = list(names)
    
    for i in range(len(nameList)):
        nameList[i] = replacement[i]

    return nameList    
    
def update_month():
    st.session_state['month'] = st.session_state.fmonth  