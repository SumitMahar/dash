import os

from dash_bootstrap_components._components.NavbarSimple import NavbarSimple
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_html_components.P import P
import pandas as pd

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
        It was rapid to develop, and trivial to host (for free) via Heroku - see the GitHub link for details. 
        """
        ),
    ]
)

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
    brand="Stock Dashboard",
    brand_href="#",
    color="dark",
    dark=True,
)

# Layout for first 2 figures
layout_1 = dbc.Row(
    className="text-center m-4",
    children=[
        dbc.Col(
            className="card card-body col-md-7 col-sm-12 shadow",
            children=[
                dcc.Checklist(
                    id="toggle-rangeslider",
                    options=[{"label": "Include Rangeslider", "value": "slider"}],
                    value=["slider"],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="graph1",
                ),
            ],
        ),
        dbc.Col(
            className="card card-body col-md-5 col-sm-12 shadow",
            children=[
                dcc.Checklist(
                    id="toggle-rangeslider2",
                    options=[{"label": "Include Rangeslider", "value": "slider"}],
                    value=["slider"],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="graph2",
                ),
            ],
        ),
    ],
)

# Layout for last 2 figures
layout_2 = dbc.Row(
    className="text-center m-4",
    children=[
        dbc.Col(
            className="card card-body col-md-6 col-sm-12 shadow",
            children=[
                dcc.Checklist(
                    id="toggle-rangeslider3",
                    options=[{"label": "Include Rangeslider", "value": "slider"}],
                    value=["slider"],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="graph3",
                ),
            ],
        ),
        dbc.Col(
            className="card card-body col-md-6 col-sm-12 shadow",
            children=[
                dcc.Checklist(
                    id="toggle-rangeslider4",
                    options=[{"label": "Include Rangeslider", "value": "slider"}],
                    value=["slider"],
                    className="bg-dark text-white",
                ),
                dcc.Graph(
                    id="graph4",
                ),
            ],
        ),
    ],
)
