import requests
from bs4 import BeautifulSoup
page= requests.get("https://ekantipur.com/").text
soup= BeautifulSoup(page, 'html.parser')

artists = soup.find_all('a')

for artist in artists:
    name = artist.get_text(strip=True)  # This gets the visible link text
    fulllink = artist.get('href') 
    print(fulllink)