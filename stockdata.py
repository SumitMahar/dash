from os import listdir, path
from posixpath import join
import pandas as pd


"""
    This file is for doing main processing of the CSV files present in the `./data` directory.
    You can add as many CSV files as you want in the `./data` directory but make sure the data 
    is in the correct format (Column names etc)
"""

# All CSV files present in the ./data directory
all_csv_files = [path.join("data", f) for f in listdir("./data") if f.endswith(".csv")]

# Merging all the csv files
try:
    stock_df = pd.concat(map(pd.read_csv, all_csv_files), ignore_index=True)
except:
    print("Error")
    stock_df = pd.DataFrame()

stock_df.set_index("Symbol", inplace=True)
stock_df["Pd_date"] = pd.to_datetime(stock_df["Date"])

SYMBOLS = [tic for tic in stock_df.index.unique()]
MIN_DATE = stock_df["Pd_date"].min()
MAX_DATE = stock_df["Pd_date"].max()

# helper function for converting big digits to human readable format
# this function is taken from stackoverflow
def make_human_readable(num):
    num = float("{:.3g}".format(num))
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return "{}{}".format(
        "{:f}".format(num).rstrip("0").rstrip("."), ["", "K", "M", "B", "T"][magnitude]
    )
