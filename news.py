import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json
from datetime import date

from datetime import datetime, timedelta


# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = os.getenv("NYTIMES_API_KEY")


def fetch_articles( api_key):
    # Base URL for the New York Times Article Search API
    BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    
    # Get current date and time
    end_date = datetime.now()
    
    # Calculate the start date (four hours ago)
    start_date = end_date - timedelta(hours=4)
    
    # Format dates as strings in the required format (YYYYMMDD)
    start_date_str = start_date.strftime('%Y%m%d')
    end_date_str = end_date.strftime('%Y%m%d')
    
    # Parameters for the API request
    params = {
        # 'q': query,  # Search query
        'api-key': api_key,
        'begin_date': start_date_str,
        'end_date': end_date_str,
    }

    # Make the API request
    response = requests.get(BASE_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and return the articles
        data = response.json()
        articles = data['response']['docs']
        return [
            {
                'abstract': article['abstract'],
                'web_url': article['web_url'],
                'snippet': article['snippet'],
                'lead_paragraph': article['lead_paragraph']
            }
            for article in articles
        ]
    else:
        print('Error:', response.status_code)
        return None


# Query for articles
# query = 'Narendra Modi'

# Fetch articles

def load_data():
    articles = fetch_articles( API_KEY)
    # Write response data to a JSON file
    if articles:
        with open('nytimes_articles.json', 'w') as f:
            json.dump(articles, f, indent=4)
        print('Articles saved to nytimes_articles.json.')
    else:
        print('No articles fetched.')










