# Taking the user's height in meters as input
height = float(input("Enter your height in meters e.g., 1.55: "))

# Taking the user's weight in kilograms as input
weight = int(input("Enter your weight in kilograms e.g., 72: "))

# Calculating the Body Mass Index (BMI)
BMI = weight / height ** 2

# Printing the BMI with two decimal places
print(f"Your BMI is {BMI:.2f}")

# Determining the weight category based on the BMI value and printing the corresponding message
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")
