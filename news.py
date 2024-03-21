import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json
from datetime import date

from datetime import datetime, timedelta

# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = os.getenv("NYTIMES_API_KEY")

# Base URL for the New York Times Article Search API
BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'


# Get today's date
# today = date.today()

# Calculate the start and end dates
end_date = datetime.now()  # Current date and time
start_date = end_date - timedelta(hours=4)  # Four hours ago

# Format dates as strings in the required format (YYYYMMDD)
start_date_str = start_date.strftime('%Y%m%d')
end_date_str = end_date.strftime('%Y%m%d')
# Parameters for the API request
params = {
    # 'q': 'Narendra Modi',  # Search query
    'api-key': API_KEY,
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
    with open('nytimes_articles.json', 'w') as f:
        json.dump(data, f, indent=4)
        
    print('Articles saved to nytimes_articles.json.')
else:
    print('Error:', response.status_code)

    
#     articles = data['response']['docs']
#     for article in articles:
#         headline = article['headline']['main']
#         content = article['lead_paragraph']  # Or use 'lead_paragraph' for longer content
#         print('Headline:', headline)
#         print('Content:', content)
#         print('------------------------')
# else:
#     print('Error:', response.status_code)