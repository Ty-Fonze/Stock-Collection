import numpy as np
import pandas as pd
from MyTT import RSI, MACD  # Importing indicators from MyTT

# Example data: Simulate a series of closing prices
close_prices = pd.Series([100, 102, 101, 105, 110, 108, 112, 115, 113, 117, 120])

# Test RSI (Relative Strength Index)
try:
    rsi_period = 14  # Typical period for RSI
    rsi_values = RSI(close_prices, N=rsi_period)
    print("RSI Values:")
    print(rsi_values)
except Exception as e:
    print(f"Error calculating RSI: {e}")

# Test MACD (Moving Average Convergence Divergence)
try:
    short_period = 12  # Fast EMA period
    long_period = 26   # Slow EMA period
    signal_period = 9  # Signal line period
    dif, dea, macd = MACD(close_prices, short=short_period, long=long_period, m=signal_period)
    print("\nMACD Results:")
    print(f"DIF: {dif}")
    print(f"DEA: {dea}")
    print(f"MACD Histogram: {macd}")
except Exception as e:
    print(f"Error calculating MACD: {e}")

# Ensure that the results match expectations by comparing with trusted sources