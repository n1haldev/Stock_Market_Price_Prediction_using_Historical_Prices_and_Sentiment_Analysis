import pandas as pd
import re
from collections import defaultdict

# Load the CSV file into a DataFrame
df = pd.read_csv('Tata Motors_news.csv')

selected_options = ['Motors', 'Nexon', 'Harrier', 'Altroz', 'Safari', 'Tiago', 'Group', 'Punch', 'Tigor', 'group', 's', 'H5X', 'Sons', 'Gravitas', 'cars', 'Hexa', '2021', 'Nano', 'HBX', 'Motor', 'IPL', 'Passenger', 'backed', 'motors', 'Buzzard', 'Projects', 'Marcopolo', 'Sierra', 'Tata', 'dealership', 'Curvv', 'H2X', 'Global', 'Mahindra', 'car', 'dealer', 'and', 'Avinya', 'unveils', 'Hornbill', 'for', 'Mercedes', 'on', 'Mint', '407', 'in', 'owned', 'rolls', 'EV', 'Red', 'foundation', 'Electric', '10', 'that', 'Is', 'hikes', 'continues', 'introduces', 'Sumo', 'chose', 'is', 'launches', 'X452', 'shares', 'AutoComp', 'plea', 'recollects', 'has', 'Jayem', 'companies', 'The', 'Discounts', 'Remembers', 'first', 'Family', 'says', 'Our', 'remembers', 'May', 'Adani', 'Essar', 'pegs', 'co', 'exec', 'provides', 'Winger', 'petrol', 'pays', 'Ultra', 'made', 'Owned', 'Super', 'EVs', 'eyes', 'builds', 'requests', 'Trucks', 'acquired', 'Why', 'discontinues', 'Xpres', 'opens', 'takes', 'Honda', 'Zest', 'Hyundai', 'Auto', 'overtakes', 'dilemma', 'Kaziranga', 'Appoints', 'as', 'brings', 'discounts', 'electric', 'arrives', 'Indica', 'Ace', 'chairman', 'removed', 'QRFV', 'ALTROZ', 'gets', 'adds', 'celebrates', 'lineup', 'Stock', 'Azura', 'boss', 'expects', 'delivers', 'Will', 'stocks', 'does', 'sells', 'Stocks', 'recounts', 'Motorsâ', 'makes']

# Initialize a list to store lines to be saved in the new CSV file
lines_to_save = []

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Tokenize the title using regular expressions
    tokens = re.findall(r'\b\w+\b', row['Titles'])
    # Find occurrences of 'Tata' in the tokens
    for i in range(len(tokens) - 1):
        if tokens[i] == 'Tata':
            # Get the word following 'Tata'
            option = tokens[i + 1]
            # Check if the option is in the selected_options list
            if option in selected_options:
                # Add the line to the list of lines to save
                lines_to_save.append(row['Titles'])

# Create a DataFrame from the lines to save
df_to_save = pd.DataFrame({'Titles': lines_to_save})

# Save the DataFrame to a new CSV file
df_to_save.to_csv('filtered_news.csv', index=False)