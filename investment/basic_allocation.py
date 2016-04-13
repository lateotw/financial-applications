"""
The objective of this tool is for anybody to be able to run the script and
figure out a sensible investment allocation level.

Disclaimer:
Use at your own risk, but I have done my best to be as transparent as
possible. Nothing here is my innovation, optimization has been used
for decades within the financial investment industry, either successfully
or unsuccessfully. With the proliferation of open source software, data
and technology, everybody should have access to a financial investment
optimizer.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime


def download_return(ticker, start, end):
    # download adjusted close price from yahoo finance

    data = web.DataReader(ticker, 'yahoo', start, end)
    log_return = np.log(data['Adj Close'] / data['Adj Close'].shift(1))
    return log_return


start_date = datetime.datetime(2010, 1, 1)
end_date = datetime.datetime.today().date()

ticker = 'AGG'

download_return(ticker, start_date, end_date).plot()

plt.show()


# Define the investment universe

# Bond: aggregate, high yield, investment grade
# bond_tickers = ['AGG', 'HYG', '?LQD']

# Equity: US large cap, US small cap, Europe, Japan, Emerging Market
# stock_tickers = ['SPY', '?russell 2000', '']

# Real Estate:

# Commodities:

# calculate individual security performance and risk


# optimizer
# target_risk = float(input("e.g. 0.10"))
# target_return = float(input("e.g. 0.10, meaning 10% per year"))
