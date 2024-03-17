age = input()  # Taking the user's age as input

# Calculating the number of years left until age 90
years_left = 90 - int(age)

# Calculating the number of weeks left based on the remaining years
weeks_left = years_left * 52

# Printing the result in the specified format
print(f"You have {weeks_left} weeks left.")
