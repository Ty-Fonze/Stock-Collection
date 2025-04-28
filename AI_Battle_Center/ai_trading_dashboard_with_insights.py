import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Initialize the app
app = dash.Dash(__name__)
app.title = "Super AI Trading Assistant"

# Function to calculate technical indicators
def calculate_indicators(data):
    # Ensure 'Close' column is present and non-empty
    if data is None or data.empty or 'Close' not in data.columns:
        raise ValueError("The 'Close' column is missing or the data is empty.")

    # Debugging: Print first few rows of the DataFrame
    print("Debug: First few rows of the input data:")
    print(data.head())

    # Ensure 'Close' column is a valid Series with numeric data
    if not pd.api.types.is_numeric_dtype(data['Close']):
        raise ValueError("The 'Close' column must contain numeric data.")

    # RSI
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    # MACD
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()

    # Bollinger Bands
    data['SMA20'] = data['Close'].rolling(window=20).mean()
    
    # Debugging: Print SMA20 to verify
    print("Debug: SMA20 column (Simple Moving Average):")
    print(data['SMA20'].head())

    # Ensure rolling_std is calculated as a Series
    rolling_std = data['Close'].rolling(window=20).std()

    # Debugging: Print rolling_std to verify
    print("Debug: Rolling standard deviation (rolling_std):")
    print(rolling_std.head())

    if rolling_std is None or not isinstance(rolling_std, pd.Series):
        raise ValueError("The rolling standard deviation is not a valid Series.")

    # Assign Bollinger Bands
    data['UpperBand'] = data['SMA20'] + (rolling_std * 2)
    data['LowerBand'] = data['SMA20'] - (rolling_std * 2)

    # Debugging: Print the final DataFrame with Bollinger Bands
    print("Debug: Final DataFrame with Bollinger Bands:")
    print(data[['SMA20', 'UpperBand', 'LowerBand']].head())

    return data

# Layout of the application
app.layout = html.Div(
    style={
        'backgroundColor': '#333333',
        'color': 'white',
        'padding': '20px',
        'fontFamily': 'Arial, sans-serif'
    },
    children=[
        html.H1("Super AI Trading Assistant", style={'textAlign': 'center'}),
        
        # Ticker Selector
        html.Div(
            [
                html.Label("Select a Stock Ticker:", style={'fontSize': '18px'}),
                dcc.Dropdown(
                    id='ticker-selector',
                    options=[
                        {'label': 'SPY (S&P 500 ETF)', 'value': 'SPY'},
                        {'label': 'AAPL (Apple)', 'value': 'AAPL'},
                        {'label': 'QQQ (NASDAQ ETF)', 'value': 'QQQ'},
                    ],
                    value='SPY',
                    clearable=False,
                    style={'width': '300px', 'color': '#000000'}
                ),
            ],
            style={'marginBottom': '20px'}
        ),
        
        # Candlestick Chart
        dcc.Graph(id='candlestick-chart'),

        # Footer
        html.Div(
            "Insights and AI-driven analysis coming soon!",
            style={'textAlign': 'center', 'marginTop': '20px', 'fontSize': '16px'}
        )
    ]
)

# Callback to update the chart based on the selected ticker
@app.callback(
    Output('candlestick-chart', 'figure'),
    [Input('ticker-selector', 'value')]
)
def update_candlestick_chart(ticker):
    # Fetch historical stock data from Yahoo Finance
    data = yf.download(ticker, period='3mo', interval='1d')  # 3-month data, daily interval

    # Debugging: Print the raw data fetched from Yahoo Finance
    print("Debug: Raw data fetched from Yahoo Finance:")
    print(data.head())

    # Check if the data is empty
    if data.empty:
        raise ValueError(f"No data returned for ticker {ticker}. Please try a different ticker.")

    # Ensure necessary columns exist
    required_columns = ['Open', 'High', 'Low', 'Close']
    for column in required_columns:
        if column not in data.columns:
            raise KeyError(f"The '{column}' column is missing in the data for ticker {ticker}.")

    # Drop rows where 'Close' is NaN
    data = data.dropna(subset=['Close'])

    # Convert 'Close' column to numeric (if necessary)
    data['Close'] = pd.to_numeric(data['Close'], errors='coerce')

    # Debugging: Print the cleaned data
    print("Debug: Cleaned data with numeric 'Close' column:")
    print(data.head())

    # Calculate indicators
    data = calculate_indicators(data)

    # Create the candlestick chart
    fig = go.Figure()

    # Add candlesticks
    fig.add_trace(
        go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name='Candlesticks'
        )
    )

    # Add Bollinger Bands
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['UpperBand'],
            line=dict(color='rgba(173,216,230,0.5)', width=1),
            name='Upper Bollinger Band',
            hoverinfo='skip'
        )
    )
    fig.add_trace(
        go.Scatter(
            x=data.index,
            y=data['LowerBand'],
            line=dict(color='rgba(173,216,230,0.5)', width=1),
            name='Lower Bollinger Band',
            hoverinfo='skip',
            fill='tonexty',  # Fill between the bands
            fillcolor='rgba(173,216,230,0.1)'
        )
    )

    # Customize the chart layout
    fig.update_layout(
        title=f"{ticker} Price Chart with Indicators (Last 3 Months)",
        xaxis_title="Date",
        yaxis_title="Price (USD)",
        template="plotly_dark",
        xaxis_rangeslider_visible=False,
        height=700
    )
    
    return fig

# Run the app
if __name__ == "__main__":
    app.run(debug=True)