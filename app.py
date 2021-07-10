import os
from re import template

import dash
from dash.dependencies import Input, Output, State
from dash_bootstrap_components._components.NavbarBrand import NavbarBrand
from dash_bootstrap_components._components.NavbarSimple import NavbarSimple
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("./data/11-07-2019-TO-09-07-2021INFYALLN.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = html.Div(
    className="container col-md-8 text-center shadow my-5",
    children=[
        dcc.Checklist(
            id="toggle-rangeslider",
            options=[{"label": "Include Rangeslider", "value": "slider"}],
            value=["slider"],
            className="bg-dark text-white",
        ),
        dcc.Graph(
            id="graph",
        ),
    ],
)


@app.callback(Output("graph", "figure"), [Input("toggle-rangeslider", "value")])
def display_candlestick(value):
    fig = go.Figure(
        go.Candlestick(
            x=df["Date"],
            open=df["Open Price"],
            high=df["High Price"],
            low=df["Low Price"],
            close=df["Close Price"],
        )
    )

    fig.update_layout(
        template="plotly_dark", xaxis_rangeslider_visible="slider" in value
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
