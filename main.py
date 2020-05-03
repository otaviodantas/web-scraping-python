from urllib.request import urlopen
from bs4 import BeautifulSoup

url_input = 'https://matchhistory.br.leagueoflegends.com/pt/#match-history/BR1/204720835' 
request   = urlopen(url_input)
only_html = request.read()

soup = BeautifulSoup(only_html, 'html.parser')
soup = soup.find ('span', {'class' : "map-mode-mode"}, id = "binding-7713")
print(soup)
