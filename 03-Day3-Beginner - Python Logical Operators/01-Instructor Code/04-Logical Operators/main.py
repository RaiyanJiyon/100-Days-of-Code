# Taking the user's age as input
age = int(input("Enter Your Age: "))

# Checking if the age is less than 18 or greater than 90
if age < 18 or age > 90:
    print("You can't Ride.")

# Checking if the age is between 18 and 90 (inclusive)
elif age >= 18 and age <= 90:
    print("You can ride.")
