import requests
from bs4 import BeautifulSoup
import lxml


def getpage(url):
    articles = []
    r = requests.get(url)
    result = BeautifulSoup(r.content, features='xml')

    items = result.findAll('item')
    for item in items:
        title = item.find('title').text
        link = item.find('link').text
        date = item.find('pubDate').text

        article = {'title': title,
                   'link': link,
                   'date': date}
        articles.append(article)

    return articles[0:5]
