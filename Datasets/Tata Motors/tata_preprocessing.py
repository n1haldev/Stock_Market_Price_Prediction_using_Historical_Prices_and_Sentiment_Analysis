import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv('Tata Motors_news.csv')

selected_options = ['Motors', 'Nexon', 'Harrier', 'Altroz', 'Safari', 'Tiago', 'Group', 'Punch', 'Tigor', 'group', 's', 'H5X', 'Sons', 'Gravitas', 'cars', 'Hexa', '2021', 'Nano', 'HBX', 'Motor', 'IPL', 'Passenger', 'backed', 'motors', 'Buzzard', 'Projects', 'Marcopolo', 'Sierra', 'Tata', 'dealership', 'Curvv', 'H2X', 'Global', 'Mahindra', 'car', 'dealer', 'and', 'Avinya', 'unveils', 'Hornbill', 'for', 'Mercedes', 'on', 'Mint', '407', 'in', 'owned', 'rolls', 'EV', 'Red', 'foundation', 'Electric', '10', 'that', 'Is', 'hikes', 'continues', 'introduces', 'Sumo', 'chose', 'is', 'launches', 'X452', 'shares', 'AutoComp', 'plea', 'recollects', 'has', 'Jayem', 'companies', 'The', 'Discounts', 'Remembers', 'first', 'Family', 'says', 'Our', 'remembers', 'May', 'Adani', 'Essar', 'pegs', 'co', 'exec', 'provides', 'Winger', 'petrol', 'pays', 'Ultra', 'made', 'Owned', 'Super', 'EVs', 'eyes', 'builds', 'requests', 'Trucks', 'acquired', 'Why', 'discontinues', 'Xpres', 'opens', 'takes', 'Honda', 'Zest', 'Hyundai', 'Auto', 'overtakes', 'dilemma', 'Kaziranga', 'Appoints', 'as', 'brings', 'discounts', 'electric', 'arrives', 'Indica', 'Ace', 'chairman', 'removed', 'QRFV', 'ALTROZ', 'gets', 'adds', 'celebrates', 'lineup', 'Stock', 'Azura', 'boss', 'expects', 'delivers', 'Will', 'stocks', 'does', 'sells', 'Stocks', 'recounts', 'Motorsâ', 'makes']

# Function to filter segments based on 'Tata' followed by an option
def filter_segments(segment):
    tokens = re.findall(r'\b\w+\b', segment)
    if 'Tata' in tokens:
        next_word_index = tokens.index('Tata') + 1
        if next_word_index < len(tokens):
            option = tokens[next_word_index]
            if option in selected_options:
                return True
    return False

# Preprocess the 'Titles' column
df['Titles'] = df['Titles'].apply(lambda x: ' | '.join(segment for segment in re.split(r'[|.]', x) if filter_segments(segment)))

# Remove rows where 'Titles' is empty
df = df[df['Titles'].str.strip() != '']

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y', errors='coerce')

# Sort the DataFrame by date
df = df.sort_values('Date')

# Save the DataFrame to a new CSV file with dates in the format 'dd-mm-yyyy'
df['Date'] = df['Date'].dt.strftime('%d-%m-%Y')
df.to_csv('filtered_news.csv', index=False)
