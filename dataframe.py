import pandas as pd
from urllib.request import urlretrieve
from my_options import URL_INPUT, HEADER
from urllib.request import urlopen
from url_handling import handling_url
from bs4 import BeautifulSoup


def captch_data(result_anuncio, result_pages):
    cards = []
    pages = int(result_pages.find(
        'span', class_='sc-1mi5vq6-0 gfpAwo').getText().split()[2])

    for interat in range(pages):
        for item in result_anuncio:
            card = {}
            card['value'] = item.find('p', 'fnmrjs-16 jqSHIm').getText()
            card['title'] = item.find('div', 'fnmrjs-8 kRlFBv').getText()
            card['location'] = item.find('p', 'fnmrjs-13 hdwqVC').getText()
            card['category'] = item.find('p', 'fnmrjs-14 iIprpQ').getText()

            # image = item.find('div', class_='fnmrjs-5 jksoiN').img.get('src')
            # urlretrieve(image, './output/img/' + image.split('/')[-1])

            cards.append(card)

    dataset = pd.DataFrame(cards)
    dataset.to_csv('./output/data/', sep=';',
                   index=False, encoding='utf-8-sig')
    print(dataset)
