# Taking the year to check as input from the user
year = int(input("Which year do you want to check? "))

# Checking if the year is divisible by 4
if year % 4 == 0:
    # If divisible by 4, checking if it's also divisible by 100
    if year % 100 == 0:
        # If divisible by 100, checking if it's also divisible by 400
        if year % 400 == 0:
            print("Leap year.")  # If divisible by 400, it's a leap year
        else:
            print("Not leap year.")  # If not divisible by 400, it's not a leap year
    else:
        print("Leap year.")  # If not divisible by 100 but divisible by 4, it's a leap year
else:
    print("Not leap year.")  # If not divisible by 4, it's not a leap year
