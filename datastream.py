import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'gsheetsdb'])

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
            "Order Profit Per Order" AS profit_per_order
        FROM
            "{0}"                     
        WHERE
            "Customer State" = 'CA' AND
            "Order Month" = 'Nov'
    """

query = template.format(source)

def data_stream():
    conn = connect()
    result = conn.execute(query, headers=1)
    
    return result