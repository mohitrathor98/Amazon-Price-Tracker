from urllib import response
import requests
from bs4 import BeautifulSoup

HEADERS = {
    # got from http://myhttpheader.com/
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}



def get_wishlist_items(wishlist_url):
    """Method to scrape wishlist and return list of dictionaries
    with item name as key and links as values
    Args:
        wishlist_url (str): url of wishlist  from items to be fetched
    """
    
    try:
        response = requests.get(url=wishlist_url, headers=HEADERS)
        #print(response.status_code)
    except:
        print("Failed to establsih connection")
        return []
    wishlist = response.text

    wish_parser = BeautifulSoup(wishlist, 'html.parser')    
    contents = wish_parser.select("h2 a")
    if contents == []:
        return []
    return [{tag.getText().strip():tag.get("href")} for tag in contents] 



def get_price_of_item(item_url):
    """Method to scrape for item's price. It returns 
    price of item provided

    Args:
        item_url (str): url of item that is to be found out
    """
    
    item_url = "https://www.amazon.in"+item_url
    try:
        response = requests.get(url=item_url, headers=HEADERS)
        #print(response.status_code)
    except:
        print("Failed to establish connection with " + item_url)
        return ""
    
    item_page = response.text
    item_page_parser = BeautifulSoup(item_page, "html.parser")

    try:
        item_price = item_page_parser.find("div", id="corePrice_feature_div").get_text()
        return item_price
    except:
        return "Error while fetching item_price"
    