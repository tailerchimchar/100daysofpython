#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters= int(input("How many letters would you like in your password?\n")) 
num_symbols = int(input(f"How many symbols would you like?\n"))
num_numbers = int(input(f"How many numbers would you like?\n"))

#Tailer's answer:
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""

for num in range(0,num_letters):
  easy_password+=letters[random.randint(0, len(letters)-1)]
for num in range(0,num_symbols):
  easy_password+=symbols[random.randint(0, len(symbols)-1)]
for num in range(0,num_numbers):
  easy_password+=numbers[random.randint(0, len(numbers)-1)]

print(f"Your new easy password is: {easy_password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ""
password_char_list = list(easy_password)
length_of_list = len(password_char_list)

# take out characters from the list 
for num in range(0, length_of_list):
  charFromList = password_char_list[random.randint(0,len(password_char_list)-1)]
  hard_password+=charFromList
  password_char_list.remove(charFromList)

print(f"Your new hard password is: {hard_password}")