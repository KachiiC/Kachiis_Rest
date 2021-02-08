from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup


def url_webscraper(url):
    u_client = urlopen(url)

    page = urlopen(url).read()

    u_client.close()

    return Soup(page, "html.parser")
