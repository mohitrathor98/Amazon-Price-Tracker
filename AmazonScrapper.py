import requests
from bs4 import BeautifulSoup

def get_wishlist_items(wishlist_url):
    """Method to scrape wishlist and return list of dictionaries
    with item name as key and links as values
    Args:
        wishlist_url (str): url of wishlist  from items to be fetched
    """
    response = requests.get(url=wishlist_url)
    wishlist = response.text

    wish_parser = BeautifulSoup(wishlist, 'html.parser')    
    contents = wish_parser.select("h2 a")
    
    return [{tag.getText().strip():tag.get("href")} for tag in contents] 