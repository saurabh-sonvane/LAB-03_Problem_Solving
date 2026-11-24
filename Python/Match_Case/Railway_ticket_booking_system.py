# Create a railway ticket booking program where users can select a train class and calculate the total ticket price.


print("1. Sleeper - ₹250")
print("2. AC 3 Tier - ₹750")
print("3. AC 2 Tier - ₹1200")
print("4. AC First Class - ₹2000")

choice = int(input("Select your class: "))
passengers = int(input("Enter number of passengers: "))

match choice:

    case 1:
        price = 250
        class_name = "Sleeper"

    case 2:
        price = 750
        class_name = "AC 3 Tier"

    case 3:
        price = 1200
        class_name = "AC 2 Tier"

    case 4:
        price = 2000
        class_name = "AC First Class"

    case _:
        price = 0
        class_name = "Invalid"

if price == 0:
    print("Invalid Class Selection")

elif passengers <= 0:
    print("Invalid Passenger Count")

else:
    total = price * passengers

    if passengers >= 5:
        discount = total * 0.10
        total -= discount

    print("Class:", class_name)
    print("Passengers:", passengers)
    print("Total Amount: ₹", total)