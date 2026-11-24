# Create an online food ordering system where users can select food items, enter quantities, and calculate their final bill.

print("1. Pizza - ₹250")
print("2. Burger - ₹120")
print("3. Pasta - ₹180")
print("4. Sandwich - ₹100")
print("5. Biryani - ₹220")

choice = int(input("Enter your choice: "))
quantity = int(input("Enter quantity: "))

match choice:

    case 1:
        item = "Pizza"
        price = 250

    case 2:
        item = "Burger"
        price = 120

    case 3:
        item = "Pasta"
        price = 180

    case 4:
        item = "Sandwich"
        price = 100

    case 5:
        item = "Biryani"
        price = 220

    case _:
        item = "Invalid"
        price = 0

if price == 0:
    print("Invalid Food Selection")

elif quantity <= 0:
    print("Invalid Quantity")

else:
    total = price * quantity

    if total > 500:
        discount = total * 0.10
        total = total - discount
    else:
        discount = 0

    print("Item:", item)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Discount:", discount)
    print("Final Bill: ₹", total)