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

#https://docs.google.com/spreadsheets/d/1_rN3lm0R_bU3NemO0s9pbFkY5LQPcuy1pscv8ZXPtg8/edit?usp=sharing
#https://docs.google.com/spreadsheets/d/1C2sP7QrIrJAii_4NZWWjtiq1rYFkxua5tkvlNHJUS0c/edit?usp=sharing

df = DataFrame(result)
AgGrid(df)
#print(df.to_dict('records'))

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