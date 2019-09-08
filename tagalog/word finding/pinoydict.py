import requests
from bs4 import BeautifulSoup

term = input("enter word to look up\n")
url = "https://tagalog.pinoydictionary.com/search?q="+term

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
definition = soup.find('div', {'class': 'definition'}).get_text()

print(definition)