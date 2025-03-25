import pandas as pd
import yfinance as yf
import mplfinance as mpf
from datetime import datetime

# Function to fetch 1-minute data and plot candlestick chart
def plot_candlestick(stock_symbol, date_str):
    # Parse the date
    date = pd.to_datetime(date_str).date()

    # Fetch 1-minute data using yfinance
    data = yf.download(tickers=stock_symbol, interval='1m', start=date_str, end=date_str)

    # Filter data for the specific date
    data['Datetime'] = pd.to_datetime(data.index)
    data['Date'] = data['Datetime'].dt.date
    data = data[data['Date'] == date]
    
    if data.empty:
        print(f"No data found for {stock_symbol} on {date_str}")
        return
    
    # Set the index to datetime for mplfinance
    data.set_index('Datetime', inplace=True)

    # Plot the candlestick chart using mplfinance
    mpf.plot(data, type='candle', style='charles', title=f'{stock_symbol} - {date_str}', ylabel='Price')

# Example usage
plot_candlestick('TATASTEEL.NS', '2024-08-01')
