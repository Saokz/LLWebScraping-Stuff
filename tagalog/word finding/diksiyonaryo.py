import requests
from bs4 import BeautifulSoup

term = input("enter word to look up\n")
url = "https://diksiyonaryo.ph/search/"+term

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
#div = soup.find('div', {'class': 'sense'}).get_text()

word = soup.find('div', {'class': 'word'}, {'id': term})
for sense in word.find_all('div', {'class': 'sense'}):
    sense_content = sense.find('div', {'class': 'sense-content'})
    definition = sense_content.find('span', {'class': 'definition'})
    print(definition.get_text())

