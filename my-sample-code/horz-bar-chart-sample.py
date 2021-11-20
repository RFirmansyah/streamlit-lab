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
AgGrid(df)

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
    options=options, height="300px",
)