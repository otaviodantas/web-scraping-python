from urllib.request import urlretrieve
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from my_options import HEADER, CONTAINER_MAIN_CARDS_FIRST, CONTAINER_MAIN_CARDS_SEC
import pandas as pd


def search_items(result_pages, result_anuncio):
    __cards = []

    for interat in range(result_pages):

        soup = interat_pages(result_pages)
        __result_anuncio = soup.find(
            'div', class_=CONTAINER_MAIN_CARDS_FIRST).findAll('div', class_=CONTAINER_MAIN_CARDS_SEC)

        for item in result_anuncio:
            card = {}
            card['value'] = item.find('p', 'fnmrjs-16 jqSHIm').getText()
            card['title'] = item.find('div', 'fnmrjs-8 kRlFBv').getText()
            card['location'] = item.find('p', 'fnmrjs-13 hdwqVC').getText()
            card['category'] = item.find('p', 'fnmrjs-14 iIprpQ').getText()

            __cards.append(card)

    return create_dataset(__cards)


def interat_pages(result_pages):
    URL = (
        'https://mg.olx.com.br/moda-e-beleza?o={}&sp=1'.format(str(result_pages + 1)))
    request = Request(URL, headers=HEADER)
    response = urlopen(request)
    html = (response.read()).decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup


def search_image(result_pages, result_anuncio):
    for interat in range(result_pages):
        for item in result_anuncio:
            image = item.find(
                'div', class_='fnmrjs-5 jksoiN').img.get('src')
            urlretrieve(image, './output/img/' + image.split('/')[-1])


def create_dataset(cards):
    dataset = pd.DataFrame(cards)
    # dataset.to_csv('\output\data', sep=';',index=False, encoding='utf-8-sig')
    return dataset


def handling_url(response):
    html = (response.read()).decode('utf-8').split()
    html = " ".join(html).replace('> <', '><')
    return html
