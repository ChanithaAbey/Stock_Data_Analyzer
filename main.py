# Import libraries; Yahoo Finance for stock data, Pandas for data manipulation, Datetime for tracking date, Matplotlib for plotting, and logging for logging messages, 
import yfinance
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import logging

# Suppress yfinance debug logs
logging.getLogger("yfinance").setLevel(logging.CRITICAL)

# Logging config for your script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetches stock data from Yahoo Finance and returns it as a Pandas DataFrame
def fetch(ticker_symbol, start_date=None, end_date=None, interval="1d"):

    try:
        if not end_date:
            end_date = datetime.now().strftime('%Y-%m-%d')
        if not start_date:
            start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

        ticker = yfinance.Ticker(ticker_symbol)
        data_frame = ticker.history(start=start_date, end=end_date, interval=interval)
        data_frame = data_frame.reset_index()

        if data_frame.empty:
            return None

        data_frame['Date'] = pd.to_datetime(data_frame['Date']).dt.date
        data_frame = data_frame.round(2)

        data_frame['SMA_50'] = data_frame['Close'].rolling(window=50).mean()
        data_frame['SMA_200'] = data_frame['Close'].rolling(window=200).mean()

        return data_frame

    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

# Ensures a valid ticker symbol is inputted 
while True:
    ticker = input("Enter a stock ticker symbol or type STOP to exit: ").upper()
    if ticker == "STOP":
        print("Program terminated")
        break

    data = fetch(ticker)

    if data is not None and not data.empty:
        max_val = data.loc[data['High'].idxmax()]
        print("Highest price details:")
        print(max_val)

        min_val = data.loc[data['Low'].idxmin()]
        print("\nLowest price details:")
        print(min_val)

        print(f"\nStock data for {ticker}:")
        print(data.head())

        name = f"{ticker}_data.csv"
        data.to_csv(name, index=False)
        print(f"\nStock data saved to {name}.")

        plt.figure(figsize=(10, 5))
        plt.plot(data['Date'], data['Close'], label='Close Price', linewidth=1.5)
        plt.plot(data['Date'], data['SMA_50'], label='SMA 50', linestyle='--')
        plt.plot(data['Date'], data['SMA_200'], label='SMA 200', linestyle=':')
        plt.title(f"{ticker} Stock Price with SMA")
        plt.xlabel("Date")
        plt.ylabel("Price in USD")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        plt.close()
        break

    else:
        print("Invalid or unavailable ticker symbol. Please try again or type STOP to exit.\n")