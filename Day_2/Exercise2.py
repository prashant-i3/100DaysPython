# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

age = input()
# Don't change code above
# write your code below this line

years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")