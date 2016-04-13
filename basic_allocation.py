"""
The objective of this tool is for anybody to be able to run the script and
figure out a sensible investment allocation level.

Disclaimer:
Use at your own risk, but I have done my best to be as transparent as
possible.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime
import math


def download_price(ticker, start, end):
    # download adjusted close price from yahoo finance

    data = web.DataReader(ticker, 'yahoo', start, end)
    return data['Adj Close'].rename(ticker)


start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime.today().date()

# Define the investment universe

bond_tickers = ['AGG',  # aggregate
                'HYG',  # high yield
                'LQD']  # investment grade


stock_tickers = ['SPY',  # US large cap
                 'IWM',  # US small cap
                 'VGK',  # Europe
                 'EWJ',  # Japan
                 'VWO']  # Emerging Market

real_estate_tickers = ['VNQ']   # REIT


all_assets = bond_tickers + stock_tickers + real_estate_tickers

# Download prices
prices = pd.DataFrame()
for ticker in all_assets:
    prices[ticker] = download_price(ticker, start_date, end_date)

# Calculate return & risk
simple_return = prices.pct_change()
asset_volatility = simple_return.std() * math.sqrt(252)
cumulative_return =
cumulative_return.plot()

# optimizer
# target_risk = float(input("e.g. 0.10"))
# target_return = float(input("e.g. 0.10, meaning 10% per year"))

#TODO: add a data feed from quandl