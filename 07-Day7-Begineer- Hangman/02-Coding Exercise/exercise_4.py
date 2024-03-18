words = ["apple", "mangoo", "jackfruits"]

import random

words_choice = random.choice(words)

print(f"The Word is {words_choice}")


user_input = input("Enter a word: ").lower()


words_length = len(words_choice)

blank = []

for _ in range(words_length):
    blank += "_"
    letter = words_choice[]

print(blank)