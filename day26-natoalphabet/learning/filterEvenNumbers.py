list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:
int_list = [int(num) for num in list_of_strings if int(num) % 2 == 0]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = 1

# Write your code 👆 above:
print(int_list)