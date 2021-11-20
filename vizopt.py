def set_donut_option(data_dict):
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
                "data": data_dict,
            }
        ],
    }
    
    return options
    
def set_bar_option(list_name,list_value):
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
            "data": list_name
          },
          "series": [
            {
              #"name": "2011",
              "type": "bar",
              "data": list_value
            }
          ]
    }
    
    return options
    
def set_line_option(list_name,list_value):
    options = {
      "xAxis": {
        "type": "category",
        "data": list_name
      },
      "yAxis": {
        "type": "value"
      },
      "series": [
        {
          "data": list_value,
          "type": "line",
          "smooth": True,
          "label": { "position": "top" }
        }
      ]
    }
    
    return options