import pandas as pd
import re

# Load the CSV file into a DataFrame
df = pd.read_csv('Tata Motors_news.csv')

selected_options = ['Motors', 'Nexon', 'Harrier', 'Altroz', 'Safari', 'Tiago', 'Group', 'Punch', 'Tigor', 'group', 's', 'H5X', 'Sons', 'Gravitas', 'cars', 'Hexa', '2021', 'Nano', 'HBX', 'Motor', 'IPL', 'Passenger', 'backed', 'motors', 'Buzzard', 'Projects', 'Marcopolo', 'Sierra', 'Tata', 'dealership', 'Curvv', 'H2X', 'Global', 'Mahindra', 'car', 'dealer', 'and', 'Avinya', 'unveils', 'Hornbill', 'for', 'Mercedes', 'on', 'Mint', '407', 'in', 'owned', 'rolls', 'EV', 'Red', 'foundation', 'Electric', '10', 'that', 'Is', 'hikes', 'continues', 'introduces', 'Sumo', 'chose', 'is', 'launches', 'X452', 'shares', 'AutoComp', 'plea', 'recollects', 'has', 'Jayem', 'companies', 'The', 'Discounts', 'Remembers', 'first', 'Family', 'says', 'Our', 'remembers', 'May', 'Adani', 'Essar', 'pegs', 'co', 'exec', 'provides', 'Winger', 'petrol', 'pays', 'Ultra', 'made', 'Owned', 'Super', 'EVs', 'eyes', 'builds', 'requests', 'Trucks', 'acquired', 'Why', 'discontinues', 'Xpres', 'opens', 'takes', 'Honda', 'Zest', 'Hyundai', 'Auto', 'overtakes', 'dilemma', 'Kaziranga', 'Appoints', 'as', 'brings', 'discounts', 'electric', 'arrives', 'Indica', 'Ace', 'chairman', 'removed', 'QRFV', 'ALTROZ', 'gets', 'adds', 'celebrates', 'lineup', 'Stock', 'Azura', 'boss', 'expects', 'delivers', 'Will', 'stocks', 'does', 'sells', 'Stocks', 'recounts', 'Motorsâ', 'makes']

# Initialize a set to store unique lines to be saved in the new CSV file
lines_to_save = set()

# Preprocess the data to filter out lines that do not contain 'Tata' followed by an option
for index, row in df.iterrows():
    # Tokenize the title using regular expressions
    tokens = re.findall(r'\b\w+\b', row['Titles'])
    # Check if 'Tata' is in the tokens
    if 'Tata' in tokens:
        # Find the word following 'Tata'
        next_word_index = tokens.index('Tata') + 1
        if next_word_index < len(tokens):
            option = tokens[next_word_index]
            # Check if the option is in the selected_options list
            if option in selected_options:
                # Add the line to the set of lines to save
                lines_to_save.add((row['Date'], row['Titles']))

# Create a DataFrame from the set of lines to save
df_filtered = pd.DataFrame(list(lines_to_save), columns=['Date', 'Titles'])

# Convert the 'Date' column to datetime format
df_filtered['Date'] = pd.to_datetime(df_filtered['Date'], format='%d-%m-%Y', errors='coerce')

# Sort the DataFrame by date
df_filtered = df_filtered.sort_values('Date')

# Save the DataFrame to a new CSV file with dates in the format 'dd-mm-yyyy'
df_filtered['Date'] = df_filtered['Date'].dt.strftime('%d-%m-%Y')
df_filtered.to_csv('filtered_news.csv', index=False)
