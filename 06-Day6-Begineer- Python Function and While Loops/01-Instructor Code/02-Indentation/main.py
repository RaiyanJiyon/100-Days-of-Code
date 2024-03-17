# Taking input for age
age = int(input("Enter your age: "))

# Defining the user-defined function
def my_function():
    print("Welcome!!")
    # Checking the age
    if age > 18:
        print("You are Elder.")
    else:
        print("You are not Elder.")
    print("Program end.")

# Calling the user-defined function
my_function()
