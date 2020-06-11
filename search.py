from urllib.request import urlretrieve
from urllib.request import Request,urlopen
from bs4 import BeautifulSoup
from my_options import HEADER
import pandas as pd


class search(object):

    def __init__(self, result_pages, result_anuncio):
        self.__pages = result_pages
        self.__main_container = result_anuncio

    def get_cards(self):
        return self.__cards

    def search_items(self):
        self.__cards = []

        for interat in range(self.__pages):

            URL = ('https://mg.olx.com.br/moda-e-beleza?o={}&sp=1'.format(str(self.__pages + 1)))
            request = Request(URL, headers=HEADER)
            response = urlopen(request)
            html = (response.read()).decode('utf-8')
            soup = BeautifulSoup(html, 'html.parser')

            self.__result_anuncio = soup.find(
                'div', class_='sc-1fcmfeb-0 WQhDk').findAll('div', class_="fnmrjs-1 ddDPXY")

            for item in self.__main_container:
                card = {}
                card['value'] = item.find('p', 'fnmrjs-16 jqSHIm').getText()
                card['title'] = item.find('div', 'fnmrjs-8 kRlFBv').getText()
                card['location'] = item.find('p', 'fnmrjs-13 hdwqVC').getText()
                card['category'] = item.find('p', 'fnmrjs-14 iIprpQ').getText()

                self.__cards.append(card)

        return self.get_cards

    def search_image(self):
        for interat in range(self.__pages):
            for item in self.__main_container:
                image = item.find(
                    'div', class_='fnmrjs-5 jksoiN').img.get('src')
                urlretrieve(image, './output/img/' + image.split('/')[-1])

    @property
    def get_dataset(self):
        return self.dataset

    def create_dataset(self):
        get_cards = self.get_cards()
        self.dataset = pd.DataFrame(get_cards)
        # self.dataset.to_csv('/output/data/', sep=';',index=False, encoding='utf-8-sig')
        return self.dataset
