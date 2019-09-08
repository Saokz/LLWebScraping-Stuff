import requests
from bs4 import BeautifulSoup

term = input("enter word to look up\n")
url = "https://tagaloglessons.com/ajax/reference_guide_search_results2.php?keyword=" + term + "&num_results=10&no_search_login=false"

data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
div = soup.find_all('div')[3].get_text()
extra = soup.find_all('div')[3].find_all('a')[2].get_text()

result = div.split(extra)[0]
print(result)
