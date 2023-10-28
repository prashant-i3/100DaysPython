# Write a program to check Leap year

# Which year do you want to check?
year = int(input())
# Write your code below this line

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")