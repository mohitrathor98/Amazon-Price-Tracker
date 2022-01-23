import AmazonScrapper

print("Fetching Wishlist...")
wishlist_url = "https://www.amazon.in/hz/wishlist/ls/2NQ950UEEK5LM"
wishlist_items = AmazonScrapper.get_wishlist_items(wishlist_url)

print(f"Fetching prices for {len(wishlist_items)} items...")
for item in wishlist_items:
    # scrape for price of item
    price = AmazonScrapper.get_price_of_item([item[key] for key in item][0]).strip()

    if price[-2:] != '00':
        continue
    
    price = price.split("₹")[1]
    
    # remove commas from price
    comma = price.count(',')
    price = list(price)
    
    while comma:
        price.remove(',')
        comma -= 1  
    price = float(''.join(price))    
    
    
        