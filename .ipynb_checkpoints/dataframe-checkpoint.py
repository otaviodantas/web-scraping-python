import pandas as pd


def captch_data(result_anuncio):
    cards = []

    def none_const(space):
        if space == None:
            card[f'{space}'] = 'NaN'
        else:
            card[f'{space}'] = space

    for item in result_anuncio:
        card = {}
        value = item.find('p', 'fnmrjs-16 jqSHIm').getText()
        none_const(value)
        title = item.find('div', 'fnmrjs-8 kRlFBv').getText()
        none_const(title)
        location = item.find('p', 'fnmrjs-13 hdwqVC').getText()
        none_const(location)
        category = item.find('p', 'fnmrjs-14 iIprpQ').getText()
        none_const(category)

        cards.append(card)

    dataset = pd.DataFrame(cards)
    print(dataset)
