def handling_url(response):
    html = (response.read()).decode('utf-8').split()
    html = " ".join(html).replace('> <', '><')
    return html
