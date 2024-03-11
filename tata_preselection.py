import pandas as pd
import re
from collections import defaultdict

# Load the CSV file into a DataFrame
df = pd.read_csv('Tata Motors_news.csv')

# Initialize an empty dictionary
tata_options = defaultdict(int)

# Iterate through each row in the DataFrame
for index, row in df.iterrows():
    # Tokenize the title using regular expressions
    tokens = re.findall(r'\b\w+\b', row['Titles'])
    # Find occurrences of 'Tata' in the tokens
    for i in range(len(tokens) - 1):
        if tokens[i] == 'Tata':
            # Get the word following 'Tata'
            option = tokens[i + 1]
            # Update the frequency in the dictionary
            tata_options[option] += 1

# Sort the dictionary by descending order of frequency
sorted_options = dict(sorted(tata_options.items(), key=lambda x: x[1], reverse=True))

# Initialize an empty list to store selected options
selected_options = []

# Iterate through each option and ask user whether to include it or not
for option, frequency in sorted_options.items():
    choice = input(f"Include '{option}' (y/n)? ")
    if choice.lower() == 'y':
        selected_options.append(option)

# Print the final list of selected options
print("Selected options:")
print(selected_options)
