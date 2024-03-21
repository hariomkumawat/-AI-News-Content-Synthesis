import requests
import xml.etree.ElementTree as ET

from dotenv import load_dotenv
load_dotenv()
import os

# Copyscape API endpoint
API_URL = 'https://www.copyscape.com/api/'

# Copyscape API credentials
USERNAME = os.getenv('COPYSCAPE_USERNAME')
API_KEY = os.getenv('COPYSCAPE_API_KEY')

def check_plagiarism(text):
    # API parameters
    params = {
        'o': 'csearch',
        'u': USERNAME,
        'k': API_KEY,
        't': text  # Text to check for plagiarism
    }

    # Make API request
    # Make API request
    response = requests.post(API_URL, data=params)

    # Parse response
    if response.status_code == 200:
        # Parse XML response
        root = ET.fromstring(response.text)
        
        # Extract relevant information from the response
        query_words = root.find('querywords').text
        cost = root.find('cost').text
        count = root.find('count').text
        all_view_url = root.find('allviewurl').text
        
        # Print the result
        print("Query Words:", query_words)
        print("Cost:", cost)
        print("Number of Matches:", count)
        print("View URL:", all_view_url)
    else:
        print('Error:', response.status_code)

# Example usage

text_to_check = """** James Crumbley Convicted of Manslaughter in Son's School Shooting**

**PONTIAC, MI –** In a historic decision, James Crumbley, father of the Oxford High School shooter, was found guilty of involuntary manslaughter on March 14, 2024, for failing to prevent the deadly incident that shocked the nation. Mr. Crumbley is now one of the first parents in the United States to be held criminally responsible for a child’s violent acts at school.

The trial, closely watched across the country, brought to light questions around gun access and parental responsibility. After 10 and a half hours of deliberation, a somber Mr. Crumbley was seen shaking his head while the verdict was read in Oakland County Court. Alongside his wife, Jennifer Crumbley, who was found guilty on identical charges earlier, the couple now faces up to 15 years in prison, with their sentencing scheduled for next month.

During the trial, prosecutors painted a damning picture of negligence. Evidence revealed t
"""


check_plagiarism(text_to_check)
