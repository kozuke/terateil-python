import requests
from bs4 import BeautifulSoup as BS

url = 'https://swallow.5ch.net/livejupiter/kako/kako0000.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BS(r.text, 'lxml')
aTag = soup.find_all('a')
for link in aTag:
    print(link.get('href'))