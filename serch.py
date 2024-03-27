from fuull_article import get_full_article
# Define the search query
# domains = ["bbc.com/news", "cnn.com", "nytimes.com","theguardian.com","reuters.com","nbcnews.com","foxnews.com","washingtonpost.com","abcnews.go.com","cbsnews.com"]  # Add the domains you want to search within
import os

import json
import requests
# API_KEY = open('API_KEY').read()

def search_articles(query):
    API_KEY = os.getenv("SEACRH_API_KEY")
    SEARCH_ENGINE_ID =os.getenv('SEARCH_ENGINE_ID')
    # search_query = 'Python tutorial'
    url = 'https://www.googleapis.com/customsearch/v1'

    article_count = 0 
    # news_sites = 'nytimes.com,bbc.com,cnn.com,example.com'
    params = {
    'q': query,
    'key': API_KEY, 
    'cx': SEARCH_ENGINE_ID,
    'lr': 'lang_en',
    # 'siteSearch': news_sites 
    }
    # Send GET request to Google Custom Search API
    response = requests.get(url, params=params)
    lst=[]
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        if 'items' in data:
            results = data['items']
            for item in results:
                # title = item['title']
                link = item['link']
                # Exclude URLs with ".pdf" in them
                if 'pdf' not in link:
                    # print("Title:", title)
                    full_art=get_full_article(link)
                    lst.append(full_art)
                    article_count += 1
                    print("Link:", link)
                    print()
                 # Break the loop if 6 articles have been appended
                if article_count == 10:
                    break
        else:
            print('No search results found.')
    else:
        print('Error:', response.status_code)

    with open('full_art.txt', 'w') as file:
        for art in lst:
            if art is not None:
                file.write(art + '\n')

        print('Article saved to full_art.txt.')



# search_query = """Last week, after testing the new, A.I.-powered Bing search engine from Microsoft, I wrote that, much to my shock, it had replaced Google as my favorite search engine. """+"NEWS"
  
# articles = search_articles(search_query)
#     # Write links to a text file
