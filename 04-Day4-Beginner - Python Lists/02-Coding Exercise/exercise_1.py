# Importing the random module
import random

# Generating a random integer (either 0 or 1)
random_integer = random.randint(0, 1)

# Checking the value of the random integer and printing "Tails" or "Heads" accordingly
if random_integer == 0:
    print("Tails")
else:
    print("Heads")
