import requests
import json
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("NYTIMES_API_KEY")
# Base URL for the New York Times Article Search API
BASE_URL = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'

# Calculate the start and end dates
end_date = datetime.now()  # Current date and time
start_date = end_date - timedelta(hours=4)  # Four hours ago

# Format dates as strings in the required format (YYYYMMDD)
start_date_str = start_date.strftime('%Y%m%d')
end_date_str = end_date.strftime('%Y%m%d')

# Parameters for the API request (specifying the date range)
params = {
    'api-key': API_KEY,
    'begin_date': start_date_str,
    'end_date': end_date_str,
}

# Make the API request
response = requests.get(BASE_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    # Extract the response data
    data = response.json()
    
    # Iterate over each article
    articles = data['response']['docs']
    for article in articles:
        # Get the URL of the article
        article_url = article['web_url']
        print(article_url)
        # Make a request to get the full content of the article
        article_response = requests.get(article_url)
        if article_response.status_code == 200:
            # Extract the full content of the article
            article_content = article_response.text
            print(article_content)
            # Save the full content of the article to a file
            article_id = article['web_url'].split('/')[-1]
            with open(f'nytimes_article_{article_id}.html', 'w', encoding='utf-8') as f:
                f.write(article_content)
                
            print(f'Article {article_id} saved.')
        else:
            print(f'Error fetching article {article_url}: {article_response.status_code}')
else:
    print('Error:', response.status_code)
