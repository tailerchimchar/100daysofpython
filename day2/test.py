print("Hello"[3])
# prints l

print(123_456_567)
# prints 123456567

# len(489) -> this throws an error

# 
two_digit_num = input("Enter only a 2 digit number: ")

first_dig = two_digit_num[0]
second_dig = two_digit_num[1]

sum = int(first_dig)+int(second_dig)
print(sum)

# python uses pemdas
height = float(input("enter your height in m: "))
weight = int(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(int(weight / (height * height)))

# other math equations
# // is floor
print(8 // 3 ) # returns 2
print(round(8/3)) # returns 3

# fstring is to combine other data types
score = 0
height = 1.8
isWinning = True

#f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

years_left = 90 - age
days_left = years_left * 365
months_left = years_left * 12
weeks_left = years_left * 52

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.)
