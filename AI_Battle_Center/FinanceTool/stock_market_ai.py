import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

    def validate_data(self, data, trusted_source):
        """
        Compare calculated indicators with a trusted source.
        """
        discrepancies = []
        for col in ['SMA', 'EMA', 'RSI', 'MACD', 'Signal Line']:
            if col in data.columns and col in trusted_source.columns:
                diff = np.abs(data[col] - trusted_source[col]).mean()
                if diff > 1e-3:  # Set an acceptable tolerance level
                    discrepancies.append(col)
                    print(f"Discrepancy found in {col}: Mean difference = {diff}")
        if discrepancies:
            print(f"Validation completed with discrepancies in: {discrepancies}")
        else:
            print("Validation successful. No discrepancies found.")
        return discrepancies

    def plot_indicators(self, data, ticker):
        """
        Plot stock prices and indicators for visualization.
        """
        try:
            plt.figure(figsize=(12, 8))
            plt.plot(data['Close'], label='Close Price', color='blue')
            if 'SMA' in data.columns:
                plt.plot(data['SMA'], label='SMA', color='orange')
            if 'EMA' in data.columns:
                plt.plot(data['EMA'], label='EMA', color='green')
            if 'RSI' in data.columns:
                plt.figure(figsize=(12, 4))
                plt.plot(data['RSI'], label='RSI', color='red')
                plt.axhline(30, linestyle='--', color='grey')
                plt.axhline(70, linestyle='--', color='grey')
            plt.title(f"Indicators for {ticker}")
            plt.legend()
            plt.show()
        except Exception as e:
            print(f"Error plotting indicators: {e}")

# Example usage
if __name__ == '__main__':
    ai = StockMarketAI()
    ticker = "AAPL"
    start_date = "2022-01-01"
    end_date = "2023-01-01"
    data = ai.fetch_historical_data(ticker, start_date, end_date)
    if data is not None:
        data = ai.calculate_sma(data)
        data = ai.calculate_ema(data)
        data = ai.calculate_rsi(data)
        data = ai.calculate_macd(data)
        ai.plot_indicators(data, ticker)