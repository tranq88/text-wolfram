import requests


def wolfram(query):

    APP_ID = 'UHVJPK-U5PJ6TXP95'
    url = f'http://api.wolframalpha.com/v1/result?appid={APP_ID}&i={query}'

    r = requests.get(url)
    return r.text


print(wolfram(input('query: ')))
