import requests
from bs4 import BeautifulSoup

term = input("enter word to look up\n")
url = "https://diksiyonaryo.ph/search/"+term

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
#div = soup.find('div', {'class': 'sense'}).get_text()

word = soup.find('div', {'class': 'word'}, {'id': term})
for sense in word.find('div', {'class': 'sense'}):

    sense_content = sense.find('div', {'class': 'sense-content'})
    print(len(sense))
        #the first "sense" div only has one element?
        #yet the second "sense" has four?

    #yet every sense is supposed to have:
        #a sense content
        #a definition
        #a definition text
    #so then what the hell?

