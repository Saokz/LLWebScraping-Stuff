import requests
from bs4 import BeautifulSoup

word = input("enter word to look up\n")
url = "https://diksiyonaryo.ph/search/"+word

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
#div = soup.find('div', {'class': 'sense'}).get_text()

wordDiv = soup.find('div', {'class': 'word'}, {'id': word}) #right. figure out how that's supposed to work.

for div in wordDiv:
    contentDiv = div.find('div', {'class': 'sense-content'})
    defDiv = contentDiv.find('span', {'class': 'definition-text'}).get_text()
    print(defDiv)
