# Printing the welcome message
print("Thank you for choosing Python Pizza Deliveries!")

# Taking user input for pizza size, pepperoni, and extra cheese
size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Initializing the price variable
price = 0

# Calculating the base price based on the pizza size
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25

# Adding the cost of pepperoni based on the pizza size
if add_pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

# Adding the cost of extra cheese
if extra_cheese == "Y":
    price += 1

# Printing the final bill
print(f"Your final bill is: ${price}.")
