import requests
from newspaper import Article

def get_full_article(url):
    # Initialize Article object
    article = Article(url)

    try:
        # Download and parse the article
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        print(f"Error fetching article: {e}")
        return None

# Example usage
# article_url = "https://www.nytimes.com/2024/03/23/world/asia/india-election-federalism.html"                                                                                                                      
# # full_article = get_full_article(article_url)

# if full_article:
#     print(full_article)
# else:
#     print("Failed to retrieve the full article.")
