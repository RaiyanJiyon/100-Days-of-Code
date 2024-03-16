# Taking input from the user for the target number
target = int(input("Enter a number between 0 and 1000: "))

# Initializing the variable to store the sum of even numbers
even_sum = 0

# Iterating through even numbers from 2 to the target number (inclusive)
for number in range(2, target + 1, 2):
    # Adding each even number to the sum
    even_sum += number

# Printing the sum of all even numbers
print(even_sum)
