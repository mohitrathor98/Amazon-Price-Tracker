import AmazonScrapper, mail, json

print("Fetching Wishlist...")
wishlist_url = "https://www.amazon.in/hz/wishlist/ls/2NQ950UEEK5LM"
wishlist_items = AmazonScrapper.get_wishlist_items(wishlist_url)

with open("prices.json", "r") as file:
        data = json.load(file)
    
if data.keys() == []:
    print("No Previous stored prices found to compare")

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
    
    item = item.keys()[0]
    if item not in data.keys():
        data[item] = price
    else:
        if data[item] > price:
            mail.send_mail({item:price})
    
with open("prices.json", "w") as file:
    json.dump(data)