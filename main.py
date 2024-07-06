## Read the API key

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv('API_KEY')

# Use the API key in your application
print(api_key)


# Make the API request
import requests
import json
symbol = "TQQQ"

url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}?apikey={api_key}"


# writing response to a CSV file
import csv
import pandas as pd
response = requests.get(url)
print(response)

# Parse the JSON response
data = response.json()

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv('output.csv', index=False)


df.head(10)
# %%
df.shape
# %%





