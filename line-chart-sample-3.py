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
AgGrid(df)

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