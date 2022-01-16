import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.amazon.in/hz/wishlist/ls/2NQ950UEEK5LM")
wishlist = response.text

wish_parser = BeautifulSoup(wishlist, 'html.parser')
print(wish_parser.select("h2 a"))