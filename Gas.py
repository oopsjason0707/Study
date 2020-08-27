import urllib.request
from bs4 import BeautifulSoup


url = "https://www.opinet.co.kr"

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')


print(soup)