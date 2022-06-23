import requests
from bs4 import BeautifulSoup
import random

a = []
title = []
link = []
# action = 'https://myanimelist.net/anime/genre/1/Action'


def anime_parser(url):
    soup = BeautifulSoup(requests.get(url).text, "lxml")
    global a
    global title
    global link

    [a.append(x.get_text().replace(' ', '')[1:-1]) for x in soup.find_all("div", title='Score')]
    [title.append(x.get_text()) for x in soup.find_all('a', class_='link-image')]
    [link.append(x.get('href')) for x in soup.find_all('a', class_='link-image')]


def anime(url, n, i=0):
    if i == 1:
        anime_parser(url)
        return title[n] + ' Оценка ' + a[n]
    return link[n]


if __name__ == "__main__":
    pass
