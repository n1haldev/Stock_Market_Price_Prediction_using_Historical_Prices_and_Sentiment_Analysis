import yfinance as yf
import pandas as pd

ticker = "HCLTECH.NS"  # Replace with the desired ticker symbol
data = yf.download(ticker, period="3y")  # Adjust period as needed
file_name = ticker + ".csv"
data.to_csv(file_name)
