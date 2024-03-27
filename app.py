import streamlit as st
import requests
import os
from dotenv import load_dotenv
load_dotenv()
import json
from datetime import date
from datetime import datetime, timedelta
from news import fetch_articles,load_data
from serch import search_articles
from ope import openaifunction
from copyscape import check_plagiarism
# Replace 'YOUR_API_KEY' with your actual API key
API_KEY = os.getenv("NYTIMES_API_KEY")



# Streamlit UI
def main():
    st.title("Article Synthesizer")

    # Text input boxes for user to input articles
    query = st.text_area("Enter Topic ")
    
    if st.button("Synthesize"):
        q=f"""{query}"""+"News"
        search_articles(q)
        # Open the text file for reading
        with open('full_art.txt', 'r') as file:
            # Read the content of the file
            Articles = file.read()

        # Print the content
        # print(content)
        title_prompt=(f"""Input Articles: {Articles}\nArticle Synthesize a new article:
            Please generate a new content article based on the provided input articles. Ensure that the synthesized article:
            - Incorporates key information from all three input articles.
            - Maintains a coherent and logical flow of information.
            - Is original and does not directly copy content from the input articles.
            - Has a length of at least [desired length] words.
            - Article length is grater then 650""")
        
        synthesized_article = openaifunction(title_prompt)
        final_data=check_plagiarism(synthesized_article)
        st.subheader("Synthesized Article")
        st.write(synthesized_article)
    




    if st.button("Get NYT Articles"):
        load_data()

    if os.path.getsize('nytimes_articles.json') == 0:
        st.error("The file is empty. Please ensure it contains data.")
    # Load the JSON data
    else:
        with open('nytimes_articles.json', 'r') as file:
            data = json.load(file)
        
        # Display abstracts from the JSON file
        st.subheader("Abstracts from NYT Articles- Last 4 hours")
        for item in data:
            abstract = item.get('abstract', 'No abstract available')
            para = item.get('lead_paragraph', 'No Paragraph available')
            st.markdown(f"**Headline:** {abstract}")
            st.markdown(f"**Paragraph:** {para}")
            st.markdown("---")

if __name__ == "__main__":
    
    main()
