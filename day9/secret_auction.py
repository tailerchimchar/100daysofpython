import os
from art import logo

print(logo)
players = []

name = input("What is your name? Type 'Exit' when you have added all bidders: ")
while name.lower() != 'exit': 
  # Clearing the Screen
  bid_amount = int(input("\nHow much do you want to bid? $"))
  new_player = {
    "Name": name,
    "Bid Amount": bid_amount,
  }
  players.append(new_player)
  os.system('cls')  

  name = input("What is your name? Type 'Exit' when you have added all bidders: ")

winner = ""
highest_bid = 0
for index in range(len(players)):
  if players[index]["Bid Amount"] > highest_bid:
    winner = players[index]["Name"]

print(f"Winner is {winner} with a bid of {highest_bid}")
