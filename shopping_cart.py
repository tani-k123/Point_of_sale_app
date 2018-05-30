# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

# print(products)


product_ids = []

message = input ("Hey please input a product identifier: ")         # accepting user inputs and then cause something to happen

while True:
    product_id = input ("Hey please input a product identifier: ")

    if product_id == "done":
        break
    else:
        product_ids.append(int(product_id))

import datetime
checkout_at = datetime.datetime.now()

print (" ")
print ("---------------------")
print ("SHOPPERS MART")      # A grocery store name of your choice.
print ("---------------------")
print ("Website: www.shoppers_mart.com")   # A grocery store phone number and/or website URL and/or address of choice.
print ("Phone: 1-800-123-MART")
print ("Checkout time: " + checkout_at.strftime("%A, %B %d, %Y at %I:%M %p"))  # The date and time of the beginning of the checkout process, formatted in a human-friendly way.
print ("---------------------")
print (" ")
print ("Products")
print ("---------------------")

#product_ids = [3, 12, 10, 3, 5, 11]

def matching_product (product_identifier):
    products_list = [p for p in products if p["id"] == product_identifier]
    return products_list [0]

raw_total = 0
# The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $1.50).
for pid in product_ids:
    product = matching_product (int(pid))
    price_format = '$ {0:.2f}'.format(product["price"])
    raw_total = raw_total + product ["price"]
    tax = raw_total * 0.08875
    total = raw_total + tax
    #product = [p for p in products if p["id"] == pid]
    print (str (product["id"]) + " " + product["name"] + " " + "(" + price_format + ")" )

raw_total_usd = '$ {0:.2f}'.format(raw_total)
tax_usd ='$ {0:.2f}'.format(tax)
total_usd = '$ {0:.2f}'.format(total)

# The amount of tax owed, calculated by multiplying the total cost by a New York City sales tax rate of 0.08875.
# The total amount owed, formatted as US dollars and cents (e.g. $1.63), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items.

print (" ")
print ("---------------------")
print ("Subtotal: " + raw_total_usd)    # The total cost of all shopping cart items, formatted as US dollars and cents (e.g. $1.50), calculated as the sum of their prices.
print ("NYS sales tax: " + tax_usd)
print ("Total due: " + total_usd)
print ("---------------------")
print (" ")

# A friendly message thanking the customer and/or encouraging the customer to shop again.
print ("Thank you for shopping at SHOPPERS MART. We look forward to seeing you again.")
