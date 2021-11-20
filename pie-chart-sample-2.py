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
AgGrid(df)

options = {
    "color": ["#7dc370", "#ffbeb2", "#fa8f79", "#b3e0a6"],
    "tooltip": {"trigger": "item"},
    "legend": {"top": "5%", "left": "center"},
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
    options=options, height="300px",
)