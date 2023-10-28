# Write a program, if your height is greater than 120cm you can ride the rollercoaster.
# if your height is less than 120cm then you can't ride

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you have to grow taller before you can ride it.")