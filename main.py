from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

try:
    url_input = 'https://matchhistory.br.leagueoflegends.com/pt/#match-history/BR1/204720835' 
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
    request   = Request(url_input, headers = header)
    response  = urlopen(request)
    html      = response.read()

except HTTPError as e:
    print(e.status, e.reason) 

except URLError as e:
    print(e.reason)

html = html.decode('utf-8')
html = " ".join(html.split()).replace('> <', '><')

soup = BeautifulSoup(html, 'html.parser')
seach = soup.findAll('div', id = 'main')
print(seach)

