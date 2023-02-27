import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import os

dash.register_page(__name__, path="/")


# Map

# Upload data.
sensors = pd.read_csv("assets/sensors.csv")

# Mapbox token
token = os.environ['DB_PWD_TER']

# Set map layout
map_layout = dict(
    mapbox={
        'accesstoken': token,
        'style': "light",
        'zoom': 12,
        'center': dict(lat=25.65409262897884, lon=-100.37682059704264)
    },
    showlegend=False,
    margin={'l': 0, 'r': 0, 'b': 0, 't': 0},
    modebar=dict(remove=["zoom", "toimage", "pan", "select", "lasso", "zoomin", "zoomout", "autoscale", "reset",
                         "resetscale", "resetview"]),
    hoverlabel_bgcolor="#000000"
)

sensors = px.scatter_mapbox(sensors, lat="lat", lon="lon", custom_data=["name", "id", "sensor_index"])

sensors.update_traces(hovertemplate="<br>".join([
    "Name: %{customdata[0]}",
    "ID: %{customdata[1]}",
    "Sensor Index %{customdata[2]}"
    ])
)

sensors.update_layout(map_layout)

# Page layout
layout = dbc.Container([

    dbc.Row(
        dbc.Col(
            dbc.Card([
                dbc.CardHeader(
                    "Air Pollution Data - San Pedro, México",
                    style={'background-color': '#FFFFFF', 'font-weight': 'bold'}
                ),
                dbc.CardBody(
                    dcc.Graph(figure=sensors,
                              config={'displaylogo': False},
                              style = {"height": "80vh", "width": "100%"}
                    )
                )
            ]),
            lg=12, className='pt-4'
        )
    )

])