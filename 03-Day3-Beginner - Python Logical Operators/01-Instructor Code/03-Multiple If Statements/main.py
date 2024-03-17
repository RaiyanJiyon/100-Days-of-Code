# Taking the user's height in centimeters as input
height = int(input("Enter Your Height in cm: "))

# Checking if the height is greater than 120 cm
if height > 120:
    print("You can Ride.")

    # Taking the user's age as input
    age = int(input("Enter Your Age: "))

    # Determining the ticket price based on age
    if age < 12:
        ticket_price = 5
    elif age < 18:
        ticket_price = 7
    else:
        ticket_price = 12

    # Asking if the user wants photos and adjusting the ticket price accordingly
    print("Want's Photos?")
    user_input = input().lower()  # Converting input to lowercase
    if user_input == "yes":
        ticket_price += 3

    # Printing the total bill
    print(f"Total bill is {ticket_price}")
else:
    print("You can't Ride.")
