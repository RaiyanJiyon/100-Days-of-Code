# 1st input: enter height in meters e.g: 1.65
height = input()

# 2nd input: enter weight in kilograms e.g: 72
weight = input()

# Converting weight to integer and height to float
weight_as_int = int(weight)
height_as_float = float(height)

# Calculating BMI using the formula: weight / (height * height)
bmi = weight_as_int / (height_as_float ** 2)

# Converting BMI to an integer
bmi_as_int = int(bmi)

# Printing the integer value of BMI
print(bmi_as_int)
