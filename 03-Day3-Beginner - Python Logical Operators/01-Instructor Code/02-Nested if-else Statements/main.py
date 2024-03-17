# Prompting the user to enter a number
num = int(input("Enter a number: "))

# Nested if-else statement to check the number's properties
if num > 0:
    # If the number is positive
    print("The number is positive.")
    if num % 2 == 0:
        # If the number is positive and even
        print("And it is even.")
    else:
        # If the number is positive and odd
        print("And it is odd.")
elif num == 0:
    # If the number is zero
    print("The number is zero.")
else:
    # If the number is negative
    print("The number is negative.")
