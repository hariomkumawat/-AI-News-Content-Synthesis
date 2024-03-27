import requests
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("BING_SUBSCRIPTION_KEY")
# Base URL for the New York Times Article Search API
BASE_URL = 'https://api.bing.microsoft.com/v7.0/news/search'

# os.environ["BING_SUBSCRIPTION_KEY"] = "559d8d604e854057a400e2ee9cf28cff"
# os.environ["BING_SEARCH_URL"] = "https://api.bing.microsoft.com/v7.0/news/search"
# Calculate the start and end dates
end_date = datetime.now()  # Current date and time
start_date = end_date - timedelta(hours=4)  # Four hours ago

# Format dates as strings in the required format (YYYYMMDD)
start_date_str = start_date.strftime('%Y%m%d')
end_date_str = end_date.strftime('%Y%m%d')

# Parameters for the API request (specifying the date range)
params = {
    'api-key': '559d8d604e854057a400e2ee9cf28cff',
    'begin_date': start_date_str,
    'end_date': end_date_str,
}

# Make the API request
response = requests.get(BASE_URL, params=params)


# Check if the request was successful
if response.status_code == 200:
    # Extract and print the headline and content of the articles
    data = response.json()
    
     # Write response data to a JSON file
    with open('bing_articles.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print('Articles saved to bing_articles.json.')
else:
    print('Error:', response.status_code)