from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as Soup


def url_webscraper(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    page = urlopen(request).read()

    return Soup(page, "html.parser")
