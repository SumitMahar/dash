import os

from dash_bootstrap_components._components.NavbarSimple import NavbarSimple
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

# Navbar
navbar = NavbarSimple(
    className="shadow text-white",
    children=[
        dbc.NavLink("About the Dashboard", className="btn btn-info text-white"),
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
