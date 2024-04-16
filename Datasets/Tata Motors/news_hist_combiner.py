import pandas as pd

df1 = pd.read_csv('TATAMOTORS.NS.csv')
df2 = pd.read_csv('Tata_Motors_news_filtered.csv')

df1['Date'] = pd.to_datetime(df1['Date'], format='%Y-%m-%d')
df2['Date'] = pd.to_datetime(df2['Date'], format='%d-%m-%Y')

merged_left = pd.merge(df1, df2, on='Date', how='left')
merged_right = pd.merge(df1, df2, on='Date', how='right')

merged_df = pd.merge(df1, df2, on='Date', how='outer')
merged_df = merged_df.sort_values(by='Date')

merged_df.to_csv('Final.csv', index=False)
