# Write a program that calculates the average student height from a List of heights.

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# Don't change the code above
# Write your code below this row
avg = 0
for n in range(0, len(student_heights)):
    avg += student[n]
