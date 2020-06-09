from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

url_input = 'https://alura-site-scraping.herokuapp.com/hello-world.php'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

response = urlopen(url=url_input)
html_only = response.read()

soup = BeautifulSoup(html_only, 'html.parser')
find = soup.find('h1', id="hello-world").get_text()

print(find)


# try:
#     request   = Request(url_input, headers = header)
#     response  = urlopen(request)

# except HTTPError as e:
#     print(e.status, e.reason)

# except URLError as e:
#     print(e.reason)

# html = response.read()
# html = html.decode('utf-8')
# html = " ".join(html.split()).replace('> <', '><')

# soup = BeautifulSoup(html, 'html.parser')
# seach = soup.find('div')
# print(seach)
