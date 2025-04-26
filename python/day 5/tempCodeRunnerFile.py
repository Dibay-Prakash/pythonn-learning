import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://ekantipur.com/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Example: Extract all links
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            print(href)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")