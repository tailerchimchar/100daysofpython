from art import logo
import random
print(logo)

random_number = random.randint(1,100)
num_of_attempts = 5 if input("Would you like to choose 'Easy' or 'Hard'?: ").lower() == "hard" else 10
print(f"You have {num_of_attempts} attempts left!")

found_number = False
counter = 0
while not found_number and counter < num_of_attempts:
  guess = int(input("Guess a number:\n"))
  if guess > random_number:
    print("Too high")
  elif guess < random_number:
    print("Too low")
  else:
    found_number = True
  counter+=1
  if not found_number:
    print(f"You have {num_of_attempts-counter} attempts left!")


if found_number:
  print(f"You found the number! The number was {random_number}")
else:
  print(f"You did not find the number! The number was {random_number}")

print(random_number)
