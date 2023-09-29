import pandas as pd
import yfinance as yf
from datetime import date, timedelta

ticker_symbol = 'META'  # change the ticker name, to see another stock

upper_band = None
lower_band = None

today = date.today()
end_date = today.strftime("%Y-%m-%d")

start_date = today - timedelta(days=1)
start_date = start_date.strftime("%Y-%m-%d")

data = yf.download(ticker_symbol, start=start_date, end=end_date, progress=False)

if not data.empty:
    current_price = data.iloc[-1]['Close']

    if upper_band is None or current_price >= 1.2 * upper_band:
        lower_band = upper_band
        upper_band = current_price
        
        upper_band_20_percent_higher = 1.2 * upper_band

    if upper_band is not None:
        lower_band = 0.8 * upper_band

    print(f"Current Live Price for {ticker_symbol}: {current_price}")
    print(f"Upper Band: {upper_band}")
    print(f"Lower Band: {lower_band}")
    print(f"20% Higher Price: {upper_band_20_percent_higher}")

    if lower_band is not None and current_price <= 0.9 * lower_band:
        print(f"Stop the loss at {current_price}")

else:
    print(f"No data available for {ticker_symbol} on {end_date}")
