# Input a list of student scores and converting them to integers
student_scores = input("Enter scores separated by space: ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Initializing the maximum score variable with the first score in the list
max_num = student_scores[0]

# Iterating through the list to find the maximum score
for score in student_scores:
    # Comparing each score with the current maximum
    if score > max_num:
        # Updating the maximum score if a higher score is found
        max_num = score

# Printing the highest score in the class
print(f"The highest score in the class is: {max_num}")
