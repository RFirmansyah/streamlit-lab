def set_donut_option(data_dict,title):
    options = {
        "title": {
          "text": title,
          "textStyle": { "fontSize": "14" }
        },
        "color": ["#fa8f79","#7dc370","#b3e0a6","#ffbeb2"],  
        "tooltip": {"trigger": "item"},
        #"legend": {"top": "5%", "left": "center"},
        "series": [
            {
                "name": "Delivery Status",
                "type": "pie",
                "radius": ["40%", "70%"],
                "avoidLabelOverlap": True,
                "itemStyle": {
                    "borderRadius": 3,
                    "borderColor": "#fff",
                    "borderWidth": 1,
                },
                #"label": {"show": True, "position": "center"},
                "emphasis": {
                    "label": {"show": True, "fontSize": "10", "fontWeight": "bold"}
                },
                "labelLine": {"show": True, "length": 10, "length2": 10},
                "data": data_dict,
                #"clockwise": True,
                "labelLayout": {"hideOverlap": False}
            }
        ],
    }
    
    return options
    
def set_bar_option(list_name,list_value,title):
    options = {
          "title": {
            "text": title,
            "textStyle": { "fontSize": "14" }
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
    
def set_line_option(list_name,list_value,title,color):
    options = {
      "title": {
        "left": "left",
        "text": title,
        "textStyle": { "fontSize": "14" }
      },
      "tooltip": {
        "trigger": "axis"
      },
      "color": [color],
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