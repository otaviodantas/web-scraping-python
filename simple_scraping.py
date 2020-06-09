from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from my_options import URL_INPUT, HEADER
from bs4 import BeautifulSoup

url_input = URL_INPUT
header = HEADER

response = (urlopen(url=url_input)).read()

soup = BeautifulSoup(response, 'html.parser')
find = soup.find('h1', id="hello-world").get_text()

print(find)
