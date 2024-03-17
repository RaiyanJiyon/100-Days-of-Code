# Importing the random module
import random

# Importing the pi_value variable from my_module
from my_module import pi_value

# Generating a random integer between 1 and 10
random_integer = random.randint(1, 10)
print(random_integer)

# Printing the value of pi from the imported module
print(pi_value)

# Generating a random float between 0 and 1
random_float = random.random()
print(random_float)

# Generating a random float between 0 and 5
random_float2 = random.random() * 5
print(random_float2)

# Generating a random love score between 1 and 100
love_score = random.randint(1, 100)
print(f"Your Love score with your partner is {love_score}")
