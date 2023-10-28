# Write a program that the digits in a 2 digit number, 
# e.g. if input is 35, then the output should be 3 + 5 = 8

two_digit_number = input()
# Don't change the code above
################################
# Write your code below this line

# # - step 1 check data type of input
# print(type(two_digit_number)) 
# 
# # this returns that our input is string
 
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# print their sum
print(first_digit + second_digit)