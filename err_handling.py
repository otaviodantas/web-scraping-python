from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from my_options import URL_INPUT, HEADER
from url_handling import handling_url
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
