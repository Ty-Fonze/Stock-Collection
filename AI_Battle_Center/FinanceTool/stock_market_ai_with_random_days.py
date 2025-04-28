import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

class StockMarketAI:
    def __init__(self):
        pass

    def fetch_historical_data(self, ticker, start_date, end_date):
        """
        Fetch historical stock data for a given ticker and date range.
        """
        try:
            stock = yf.Ticker(ticker)
            historical_data = stock.history(start=start_date, end=end_date)
            print(f"Fetched historical data for {ticker}.")
            return historical_data
        except Exception as e:
            print(f"Error fetching historical data for {ticker}: {e}")
            return None

    def calculate_sma(self, data, window=20):
        """
        Calculate Simple Moving Average (SMA).
        """
        data['SMA'] = data['Close'].rolling(window=window).mean()
        print(f"Calculated {window}-day SMA.")
        return data

    def calculate_ema(self, data, window=20):
        """
        Calculate Exponential Moving Average (EMA).
        """
        data['EMA'] = data['Close'].ewm(span=window, adjust=False).mean()
        print(f"Calculated {window}-day EMA.")
        return data

    def calculate_rsi(self, data, window=14):
        """
        Calculate Relative Strength Index (RSI).
        """
        delta = data['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        print(f"Calculated {window}-day RSI.")
        return data

    def calculate_macd(self, data, fast=12, slow=26, signal=9):
        """
        Calculate MACD (Moving Average Convergence Divergence).
        """
        data['MACD'] = data['Close'].ewm(span=fast, adjust=False).mean() - \
                       data['Close'].ewm(span=slow, adjust=False).mean()
        data['Signal Line'] = data['MACD'].ewm(span=signal, adjust=False).mean()
        data['MACD Histogram'] = data['MACD'] - data['Signal Line']
        print(f"Calculated MACD with fast={fast}, slow={slow}, signal={signal}.")
        return data

    def display_random_days(self, data, num_days=50):
        """
        Display SMA, EMA, RSI, and MACD for random trading days.
        """
        # Ensure we only select from days with complete data
        valid_data = data.dropna(subset=['SMA', 'EMA', 'RSI', 'MACD', 'Signal Line'])
        random_days = valid_data.sample(n=num_days, random_state=42)  # Use random_state for reproducibility
        random_days = random_days.sort_index()  # Sort by date for easier reading

        print("\n--- Randomly Selected Days ---")
        for date, row in random_days.iterrows():
            print(f"Date: {date.date()}")
            print(f"  Close: {row['Close']:.2f}")
            print(f"  SMA: {row['SMA']:.2f}")
            print(f"  EMA: {row['EMA']:.2f}")
            print(f"  RSI: {row['RSI']:.2f}")
            print(f"  MACD: {row['MACD']:.2f}")
            print(f"  Signal Line: {row['Signal Line']:.2f}")
            print("-" * 30)

        return random_days

# Example usage
if __name__ == '__main__':
    ai = StockMarketAI()
    ticker = "AAPL"  # You can change this to another ticker
    start_date = "2022-01-01"
    end_date = "2023-01-01"

    # Fetch historical data
    data = ai.fetch_historical_data(ticker, start_date, end_date)

    if data is not None:
        # Calculate indicators
        data = ai.calculate_sma(data)
        data = ai.calculate_ema(data)
        data = ai.calculate_rsi(data)
        data = ai.calculate_macd(data)

        # Display 50 random days for validation
        ai.display_random_days(data, num_days=50)