# تعريف المنتجات (الاسم - السعر - الكمية - الوزن - هل يحتاج شحن)
products = {
    "Cheese": {"price": 200, "quantity": 10, "weight": 200, "shipping": True},
    "Biscuits": {"price": 150, "quantity": 5, "weight": 700, "shipping": True},
    "ScratchCard": {"price": 50, "quantity": 20, "weight": 0, "shipping": False},
    "TV": {"price": 5000, "quantity": 5, "weight": 0, "shipping": False}
}

# رصيد العميل
customer_balance = 1000

# السلة
cart = [
    {"name": "Cheese", "quantity": 2},
    {"name": "Biscuits", "quantity": 1},
    {"name": "ScratchCard", "quantity": 1}
]

# حساب الوزن و الفاتورة
shipping_items = []
subtotal = 0

for item in cart:
    name = item["name"]
    quantity = item["quantity"]
    product = products[name]
    
    if quantity > product["quantity"]:
        print(f"Error: {name} is out of stock")
        exit()

    price = product["price"]
    subtotal += price * quantity
    
    if product["shipping"]:
        total_weight = quantity * product["weight"]
        shipping_items.append((f"{quantity}x {name}", total_weight))

# رسوم الشحن
shipping_fee = 30
total_amount = subtotal + shipping_fee

if customer_balance < total_amount:
    print("Error: Customer balance is insufficient")
    exit()

# طباعة بيانات الشحن
print("** Shipment notice **")
total_weight = 0
for name, weight in shipping_items:
    print(f"{name} {weight}g")
    total_weight += weight
print(f"Total package weight {round(total_weight / 1000, 1)}kg")

# طباعة الفاتورة
print("\n** Checkout receipt **")
for item in cart:
    name = item["name"]
    quantity = item["quantity"]
    price = products[name]["price"]
    print(f"{quantity}x {name}\t{price}")
print("----------------------")
print(f"Subtotal\t{subtotal}")
print(f"Shipping\t{shipping_fee}")
print(f"Amount\t\t{total_amount}")
