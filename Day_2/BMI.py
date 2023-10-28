# Write a program that calculates the Body Mass index(BMI) from a user's weight and height.
# BMI = weight(kg) / height * height (m sq.)

# 1st input : enter height in meters e.g: 1.65
height = input("Height : ")
# 2nd input : enter weight in kilograms e.g: 72
weight = input("Weight : ")
# Don't change the code above
################################
# write your code below this line
height_int = float(height)
weight_int = int(weight)

BMI = (weight_int / height_int ** 2)

print(BMI)