# Printing the welcome message
print("Welcome to the roller-coaster!")

# Taking the user's height in centimeters as input
height = int(input("What is your height in cm? "))

# Checking if the height is equal to or greater than 120 cm
if height >= 120:
    # Printing the message indicating the user can ride the rollercoaster
    print("You can ride the rollercoaster!")
else:
    # Printing the message indicating the user needs to grow taller to ride
    print("You have to grow taller before you can ride.")
