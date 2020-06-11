from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from my_options import URL_INPUT, HEADER
from url_handling import handling_url
from search import search
from bs4 import BeautifulSoup

url_input = URL_INPUT
header = HEADER

try:
    request = Request(url_input, headers=header)
    response = urlopen(request)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

html_clean = handling_url(response)
soup = BeautifulSoup(html_clean, 'html.parser')

result_anuncio = soup.find(
    'div', class_='sc-1fcmfeb-0 WQhDk').findAll('div', class_="fnmrjs-1 ddDPXY")

result_pages = soup.find(
    'div', class_='col2 sc-15vff5z-5 fFdJjk').find('div', class_="sc-jTzLTM sc-ksYbfQ uUqze")
result_pages = int(result_pages.find(
    'span', class_='sc-1mi5vq6-0 gfpAwo').getText().split()[2])

return_data = search(result_pages, result_anuncio)
items = return_data.search_items()
data = return_data.create_dataset()
# image = return_data.search_image()

print(data)
