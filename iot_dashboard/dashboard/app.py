import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import requests

API_URL = "http://127.0.0.1:8000/data"

app = dash.Dash(__name__)
app.title = "Air Quality Monitor"

app.layout = html.Div([
    html.H1("Air Quality Indexing &` Monitoring System"),

    dcc.Interval(
        id="interval-component",
        interval=5000,
        n_intervals=0
    ),
    dcc.Graph(id="temp-humidity"),
    dcc.Graph(id="pm-graph"),
    dcc.Graph(id="particle-bar"),
])

def fetch_data():
    try:
        response = requests.get(API_URL)
        return pd.DataFrame(response.json())
    except:``
        return pd.DataFrame()
    
@app.callback(
    [Output("temp-humidity", "figure"),
     Output("pm-graph", "figure"),
     Output("particle-bar", "figure")],
     [Input("interval-component", "n_intervals")]
)
def update_graphs(n):
    df = fetch_data()

    if df.empty:
        return{}, {}, {}
    
    #temperature and humidity
    temp_fig = go.Figure()
    temp_fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["temperature"],
        name="Temperature (C)"
    ))
    temp_fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["humidity"],
        name="Humidity (%)"
    ))
    temp_fig.update_layout(title="Temperature & Humidity")

    #particulate matter graph
    pm_fig = go.Figure()
    pm_fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["pm1_atm"],
        name="PM1.0"
    ))
    pm_fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["pm25_atm"],
        name="PM2.5"
    ))
    pm_fig.add_trace(go.Scatter(
        x=df["timestamp"],
        y=df["pm10_atm"],
        name="PM10"
    ))
    pm_fig.update_layout(title="Particulate Matter (ATM)", yaxis_title="ug/m3")


    #particulate Bar Chart
    latest = df.iloc[-1]
    particle_bar = go.Figure(data=[
        go.Bar(
            x=[">0.3", ">0.5",">1.0",">2.5",">5.0",">10"],
            y=[
                latest["pc_03"],
                latest["pc_05"],
                latest["pc_10"],
                latest["pc_25"],
                latest["pc_50"],
                latest["pc_100"]
            ]
        )
    ])
    particle_bar.update_layout(
        title = "Particle Count Distribution (latest)",
        yaxis_title="Particles / 0.1L"
    )

    return temp_fig, pm_fig, particle_bar

if __name__ == "__main__":
    app.run(debug = True, port = 8050)