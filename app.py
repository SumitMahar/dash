import os

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd

from layout import layout_1, layout_2, navbar


df = pd.read_csv("./data/11-07-2019-TO-09-07-2021INFYALLN.csv")

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css",
]

app = dash.Dash(__name__, title="Py-Dash", external_stylesheets=external_stylesheets)
# Main layout of the app
app.layout = html.Div(className="", children=[navbar, layout_1, layout_2])

# Callback function for bootstrap Modal
@app.callback(
    Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("close", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open


@app.callback(
    Output("graph1", "figure"),
    [Input("toggle-rangeslider", "value")],
)
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
