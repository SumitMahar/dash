import os

from dash_bootstrap_components._components.NavbarSimple import NavbarSimple
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

from stockdata import SYMBOLS, MIN_DATE, MAX_DATE


# Options for dropdown menu
# label: user sees | value : script sees
options = [{"label": tic, "value": tic} for tic in SYMBOLS]

# Description for bootstrap Modal
about_dashboard = html.Div(
    children=[
        html.A(
            [html.I(className="fa fa-bar-chart mx-1"), "Data Source (nse)"],
            href="https://www1.nseindia.com/products/content/equities/equities/eq_security.htm",
            className="btn btn-outline-info shadow mb-3 mr-2",
        ),
        html.A(
            [html.I(className="fa fa-github mx-1"), "Github Repository"],
            href="https://github.com/SumitMahar/dash",
            className="btn btn-dark shadow mb-3",
        ),
        html.P(
            """
            *The Content on this site is for informational purposes only and to illustrates what is possible using 
        the Open Source & free Python data visualisation library Plotly Dash.
        The code is entirely Open Source, and is intended as a showcase of what is possible 
        in very few lines of python Plotly Dash code.
        Code is available on github.
        """,
            className="text-muted",
        ),
        html.P(
            """
        This is rapid app development: not intended for 'production', more for prototyping.
        Think of it as a completely free Tableau, with the power of python for data science
        & machine learning directly accessible. The source code is in the GitHub link above.
        """
        ),
        html.P(
            """
        The dashboard is optimised for desktop or laptop.
        """
        ),
        html.P(
            """
        To save any plot locally, use the camera icon in top left. 
        """
        ),
        html.P(
            """
        All plots are interactive -hover over charts, lines & points 
        for tooltips (dynamic annotations), zoom using your mouse (drag to select area to 
        zoom into), and double click to zoom out & reset. 
        """
        ),
        html.P(
            """
        See the GitHub link for details.
        (Reach me at SumitMahar78@gmail.com)
        """
        ),
    ]
)

# Modal code taken from official dash-bootstrap documentation
modal = html.Div(
    [
        dbc.Button(
            "About the Dashboard", id="open", n_clicks=0, className="btn btn-info"
        ),
        dbc.Modal(
            [
                dbc.ModalHeader("Stock Dashboard | NSE Data"),
                dbc.ModalBody(children=about_dashboard),
                dbc.ModalFooter(
                    dbc.Button("Close", id="close", className="ml-auto", n_clicks=0)
                ),
            ],
            id="modal",
            is_open=False,
            size="lg",
        ),
    ]
)

# Navbar
navbar = NavbarSimple(
    className="shadow text-white",
    children=[
        # dbc.NavLink("About the Dashboard", className="btn btn-info text-white", id='open'),
        modal,
        dbc.NavLink(
            [
                html.I(className="fa fa-github mx-1"),
                "Github",
            ],
            href=r"https://github.com/SumitMahar/dash",
        ),
        dbc.NavLink(
            [html.I(className="fa fa-linkedin-square mx-1"), "Linked In"],
            href="https://linkedin.com/in/sumit-mahar",
        ),
    ],
    brand="Stock Dashboard ( IT sector )",
    brand_href="/",
    color="dark",
    dark=True,
)

# Layout for first 2 figures
layout_1 = dbc.Row(
    className="text-center m-4",
    children=[
        # First col
        dbc.Col(
            className="card card-body col-md-7 col-sm-12 shadow",
            children=[
                # Div for dropdown and checklist
                html.Div(
                    [
                        # Div for dropdown field
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select a stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                dcc.Dropdown(
                                    id="ticker",
                                    options=options,
                                    value=options[0]["label"],
                                    className="text-dark",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        # Div for checklist
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="toggle-rangeslider",
                                    options=[
                                        {
                                            "label": "Include Rangeslider",
                                            "value": "slider",
                                        }
                                    ],
                                    value=["slider"],
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    # class for drowpdown and checklist div
                    className="bg-dark text-white",
                ),
                # figure stuff
                dcc.Graph(
                    id="graph1",
                ),
            ],
        ),
        # 2nd col
        dbc.Col(
            className="card card-body col-md-5 col-sm-12 shadow",
            children=[
                # Div for dropdown and checklist
                html.Div(
                    [
                        # Div for dropdown field
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                # will be able to select multiple stock symbols (will be returned as list to callback function)
                                dcc.Dropdown(
                                    id="multi_tickers",
                                    options=options,
                                    value=[op["label"] for op in options[:2]],
                                    className="text-dark",
                                    multi=True,
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        # Div for checklist
                        html.Div(
                            [
                                dcc.Checklist(
                                    id="toggle-rangeslider2",
                                    options=[
                                        {
                                            "label": "Include Rangeslider",
                                            "value": "slider",
                                        }
                                    ],
                                    value=["slider"],
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    # class for drowpdown and checklist div
                    className="bg-dark text-white",
                ),
                # plotly figure (line chart)
                dcc.Graph(
                    id="line_chart",
                ),
            ],
        ),
    ],
)

# Layout for last 2 figures
layout_2 = dbc.Row(
    className="text-center m-4 justify-content-md-center",
    children=[
        # 1st col
        dbc.Col(
            className="card card-body col-md-6 col-sm-12 shadow",
            children=[
                # Div for dropdown options and date picker range
                html.Div(
                    [
                        # Div for dropdown field
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                # will be able to select single stock (will be returned as str to callback function)
                                dcc.Dropdown(
                                    id="bar_ticker",
                                    options=options,
                                    value=options[0]["label"],
                                    className="text-dark",
                                ),
                                # Div for date picker
                                html.Div(
                                    [
                                        dcc.DatePickerRange(
                                            id="bar_date_picker",
                                            min_date_allowed=MIN_DATE,
                                            max_date_allowed=MAX_DATE,
                                            start_date=MAX_DATE - pd.Timedelta(days=3),
                                            end_date=MAX_DATE,
                                            className="d-inline",
                                        ),
                                    ],
                                    className="d-inline col-md-6",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    # class for drowpdown and checklist div
                    className="bg-dark text-white",
                ),
                # Pie chart
                dcc.Graph(
                    id="bar_graph",
                ),
            ],
        ),
        # 2nd col
        dbc.Col(
            className="card card-body col-md-6 col-sm-12 shadow",
            children=[
                html.Div(
                    [
                        # Div for dropdown field
                        html.Div(
                            [
                                html.P(
                                    [
                                        html.I(className="fa fa-line-chart mr-1"),
                                        "Select stock symbol",
                                    ],
                                    className="d-inline mr-2",
                                ),
                                # will be able to select multiple stock symbols (will be returned as list to callback function)
                                dcc.Dropdown(
                                    id="pie_tickers",
                                    options=options,
                                    # upto 3 symbols will be selected on the loading (options: list of dict)
                                    value=[op["label"] for op in options[:3]],
                                    className="text-dark",
                                    multi=True,
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                        # Div for date picker
                        html.Div(
                            [
                                dcc.DatePickerSingle(
                                    id="pie_date_picker_single",
                                    min_date_allowed=MIN_DATE,
                                    max_date_allowed=MAX_DATE,
                                    date=MAX_DATE,
                                    className="d-inline",
                                ),
                            ],
                            className="d-inline col-md-6",
                        ),
                    ],
                    # class for drowpdown and checklist div
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="pie_chart",
                ),
            ],
        ),
    ],
)
