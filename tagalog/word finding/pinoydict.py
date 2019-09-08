import requests
from bs4 import BeautifulSoup

word = input("enter word to look up\n")
url = "https://tagalog.pinoydictionary.com/search?q="+word

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
div = soup.find('div', {'class': 'definition'}).get_text()

print(div)