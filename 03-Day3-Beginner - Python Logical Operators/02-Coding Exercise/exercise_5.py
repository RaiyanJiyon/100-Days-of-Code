print("The Love Calculator is calculating your score...")
name1 = input().lower()  # What is your name?
name2 = input().lower()  # What is their name?

# Count occurrences of letters in the words TRUE and LOVE
true_count = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e')
love_count = name1.count('l') + name1.count('o') + name1.count('v') + name1.count('e')

true_count += name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e')
love_count += name2.count('l') + name2.count('o') + name2.count('v') + name2.count('e')

# Combine counts to make a two-digit number
love_score = int(str(true_count) + str(love_count))

# Check love score and print the result
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
