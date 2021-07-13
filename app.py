import os

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from plotly import express as px
import pandas as pd
from datetime import datetime as dt

from layout import layout_1, layout_2, navbar
from stockdata import stock_df, make_human_readable

# Css  stylesheet
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


# Candlestick chart for single symbol
@app.callback(
    Output("graph1", "figure"),
    [Input("ticker", "value"), Input("toggle-rangeslider", "value")],
)
def display_candlestick(ticker, value):
    df = stock_df[stock_df.index == ticker]

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
        template="plotly_dark",
        title=ticker,
        yaxis_title="Price (INR)",
        xaxis_title="Date",
        xaxis_rangeslider_visible="slider" in value,
    )
    return fig


# Line chart for multiple selected symbols
@app.callback(
    Output("line_chart", "figure"),
    [Input("multi_tickers", "value"), Input("toggle-rangeslider2", "value")],
)
def display_line_chart(tickers, value):
    fig = go.Figure()

    # List comprehension to create trace for fig objects because
    # tickers is a list and it can have only one element also so
    # if someone selects multiple symbols it will create multiple line charts accordingly
    traces = [
        go.Scatter(
            x=stock_df["Date"],
            y=stock_df[stock_df.index == tic]["Close Price"],
            mode="lines",
            name=tic,
        )
        for tic in tickers
    ]

    fig.add_traces(traces)
    fig.update_layout(
        template="plotly_dark",
        title=", ".join(tickers),
        yaxis_title="Price (INR)",
        xaxis_title="Date",
        xaxis_rangeslider_visible="slider" in value,
    )
    return fig


# bar graph for Total traded quantity vs Deliverable quantity
@app.callback(
    Output("bar_graph", "figure"),
    [
        Input("bar_ticker", "value"),
        Input("bar_date_picker", "start_date"),
        Input("bar_date_picker", "end_date"),
    ],
)
def display_bar_graph(bar_ticker, start_date, end_date):
    df = stock_df[
        (stock_df.index == bar_ticker)
        & (stock_df["Pd_date"] >= pd.to_datetime(start_date))
        & (stock_df["Pd_date"] <= pd.to_datetime(end_date))
    ]

    fig = go.Figure(
        [
            go.Bar(
                name="Total",
                x=df["Date"],
                y=df["Total Traded Quantity"],
                text=df["Total Traded Quantity"],
                textposition="auto",
            ),
            go.Bar(
                name="Deliverable",
                x=df["Date"],
                y=df["Deliverable Qty"],
                text=df["Deliverable Qty"],
                hovertext=df["% Dly Qt to Traded Qty"],
                textposition="auto",
            ),
        ]
    )

    fig.update_layout(
        template="plotly_dark",
        title="Total traded Qty vs Deliverable Qty",
        barmode="group",
    )
    return fig


# Pie chart for turnover data
@app.callback(
    Output("pie_chart", "figure"),
    [Input("pie_tickers", "value"), Input("pie_date_picker_single", "date")],
)
def display_pie_chart(pie_tickers, date):
    values = [
        float(
            stock_df[
                (stock_df.index == tic) & (stock_df["Pd_date"] == pd.to_datetime(date))
            ]["Turnover"]
        )
        for tic in pie_tickers
    ]
    # make_human_readable(999999) -> 1M
    human_readable = list(map(make_human_readable, values))

    fig = go.Figure(
        go.Pie(
            labels=pie_tickers,
            values=values,
            text=human_readable,
            textinfo="text+percent",
            opacity=0.9,
            # pull: has been set to highlight the min turnover
            pull=[0.1 if v == min(values) else 0 for v in values],
        )
    )

    fig.update_layout(
        template="plotly_dark",
        title=f"Turnover % and amount ( INR ) on {pd.to_datetime(date).date()}",
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
