from art import logo, vs
import os 
from game_data import data
import random

def game(score):
  print(logo)
  random_person_1 = random.choice(data)
  random_person_2 = random.choice(data) 
  if random_person_2 == random_person_1:
    random_person_2 = random.choice(data)
  should_continue = True
  while should_continue:
    os.system('cls')  


    print(logo)
    print(f"Score: {score}")
    p1_followers = random_person_1["follower_count"]
    p1_description = random_person_1["description"]
    p1_name = random_person_1["name"]
    p1_country = random_person_1["country"]

    p2_followers = random_person_2["follower_count"]
    p2_description = random_person_2["description"]
    p2_name = random_person_2["name"]
    p2_country = random_person_2["country"]

    # Describe them both. Have person 1's followers show up, ask if they think person 2 has higher or lower
    print(f"{p1_name}, birthed in {p1_country}, a {p1_description.lower()}, has {p1_followers} followers.")
    print(vs + "\n")
    choice = input(f"{p2_name}, birthed in {p2_country}, a {p2_description.lower()}, has higher or lower followers?: ")
    print(f"{p1_name} has {p1_followers}")
    print(f"{p2_name} has {p2_followers}")
    if choice.lower() == "higher":
      if p2_followers > p1_followers:
        print("\nYou win!")
        random_person_1 = random_person_2
        random_person_2 = random.choice(data)
        score += 1
      else: 
        print("\nYou lose :(!")
        should_continue = False

    elif choice.lower() == "lower":
      if p2_followers < p1_followers:
        random_person_2 = random.choice(data)        
        score += 1
      else: 
        print("\nYou lose :(!")
        should_continue = False
    # should_continue = True
  return score
  
player_keeps_playing = True
while player_keeps_playing:
  score = 0
  score = game(score)
  print(f"score is: {score}" )
  player_keeps_playing = True if input("Do you want to keep playing? y or n: ").lower() == 'y' else False