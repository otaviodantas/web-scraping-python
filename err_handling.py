from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from my_options import URL_INPUT, HEADER \
    ,CONTAINER_PAGES_FIRST, CONTAINER_PAGES_SEC \
    , CONTAINER_MAIN_CARDS_FIRST, CONTAINER_MAIN_CARDS_SEC \
    , CONTAINER_PAGES_THIRD
from all_def import search_items, handling_url, create_dataset
from bs4 import BeautifulSoup

try:
    request = Request(URL_INPUT, headers=HEADER)
    response = urlopen(request)

except HTTPError as e:
    print(e.status, e.reason)

except URLError as e:
    print(e.reason)

html_clean = handling_url(response)
soup = BeautifulSoup(html_clean, 'html.parser')

result_anuncio = soup.find(
    'div', class_ = CONTAINER_MAIN_CARDS_FIRST).findAll('div', class_ = CONTAINER_MAIN_CARDS_SEC)

result_pages = soup.find('div', class_ = CONTAINER_PAGES_FIRST).find('div', class_ = CONTAINER_PAGES_SEC)
result_pages = int(result_pages.find(
    'span', class_= CONTAINER_PAGES_THIRD).getText().split()[2])

return_data = search_items(result_pages, result_anuncio)
# image = return_data.search_image()

print(return_data)
