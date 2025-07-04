# Define products
products = {
    "Cheese": {"price": 200, "qty": 10, "weight": 200, "shippable": True},
    "Biscuits": {"price": 150, "qty": 5, "weight": 700, "shippable": True},
    "ScratchCard": {"price": 50, "qty": 20, "weight": 0, "shippable": False},
    "TV": {"price": 5000, "qty": 5, "weight": 0, "shippable": False}
}

customer_balance = 1000

# Items in cart
cart = [
    {"name": "Cheese", "qty": 2},
    {"name": "Biscuits", "qty": 1},
    {"name": "ScratchCard", "qty": 1}
]

shipping_items = []
subtotal = 0

# Calculate subtotal and shipping items
for item in cart:
    name = item["name"]
    qty = item["qty"]
    product = products[name]

    if qty > product["qty"]:
        print(f"Error: {name} is out of stock")
        exit()

    price = product["price"]
    subtotal += price * qty

    if product["shippable"]:
        total_weight = qty * product["weight"]
        shipping_items.append((f"{qty}x {name}", total_weight))

shipping_fee = 30
total_amount = subtotal + shipping_fee

if customer_balance < total_amount:
    print("Error: Customer balance is insufficient")
    exit()

# Print shipping info
print("** Shipment notice **")
total_weight = 0
for name, weight in shipping_items:
    print(f"{name} {weight}g")
    total_weight += weight
print(f"Total package weight {round(total_weight / 1000, 1)}kg")

# Print receipt
print("\n** Checkout receipt **")
for item in cart:
    name = item["name"]
    qty = item["qty"]
    price = products[name]["price"]
    print(f"{qty}x {name}\t{price}")
print("----------------------")
print(f"Subtotal\t{subtotal}")
print(f"Shipping\t{shipping_fee}")
print(f"Amount\t\t{total_amount}")
