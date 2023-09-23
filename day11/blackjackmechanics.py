import random 
import os
import blackjackplayerchoices
bj_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_player(players, count):
  player = input(f"What is the player {count+1}'s name?: ")
  total_money = int(input(f"What player's buyin?: "))
  current_hand = []
  players[player] = {
    "Name": player,
    "Money": total_money,
    "Hand": current_hand,
    "Bet": 0,
    "Already_Won": False
  }

def give_cards(hand):
  hand.append(random.choice(bj_deck))
  return hand

def initial_give_cards(hand):
  for i in range(2):
    hand.append(random.choice(bj_deck))
  return hand

def deal_dealer():
  dealer = {
    "Name": "Dealer",
    "Money": 1000000000000000,
    "Hand": [random.choice(bj_deck), random.choice(bj_deck)],
  }
  return dealer

def calculate_total(person):
  sum = 0
  for num in person:
    sum+=num
  return sum

def dealer_plays(dealer_hand):
  #input("Press enter to see the dealer's card...")
  should_continue = False
  dealer_bust = False
  while not should_continue:
    #input("Press enter to see the dealer's card...")
    sum = calculate_total(dealer_hand)
    print(f"Dealer's hand is {dealer_hand}")
    if sum == 17 or sum == 18 or sum == 19 or sum == 20 or sum == 21:
      should_continue = True
    elif sum > 21:
      should_continue = True
    else:
      blackjackplayerchoices.hit(dealer_hand)
   

def playersVsDealer(players_in, dealer):
  if len(players_in) == 0:
    print("No players are playing lol. Moving on.")
  else:
    print(f"Dealer's hand is: {dealer['Hand']}")
    input("Press enter to see the dealer's card...")
    dealer_plays(dealer["Hand"])
    dealer_total = calculate_total(dealer["Hand"])
    player_total = 0
    if dealer_total > 21:
      for player in players_in:
        player_win(players_in, player)
    else:
      for player in players_in:    
        player_total = calculate_total(players_in[player]["Hand"]) 
        if dealer_total < player_total:
          player_win(players_in, player)
        else:
          player_lose(players_in,player)

def instant_blackjack(person):
  current_hand_score = person["Hand"][0] + person["Hand"][1]
  # print(f'{ person["Hand"][0]} + {person["Hand"][1]} = {person["Hand"][0] + person["Hand"][1]}')
  if current_hand_score == 21:
    return True
  return False

random_person = {
  "Name": "tailer",
  "Money": 20,
  "Hand": [10,11]
}

def give_players_cards(players):
  for player in players:
    bet = int(input(f"How much would {players[player]['Name'].title()} like to bet?: "))
    if bet > players[player]["Money"]:
      print("Hey! You can't bet that much. You're out of this bet.")
    else:
      players[player]["Bet"] = bet
      initial_give_cards(players[player]["Hand"])
      if instant_blackjack(players[player]):
        players[player]['Money']+= bet * 1.5
        players[player]["Already_Won"] = True
        print(f"Wow! You're lucky!\n {players[player]['Name'].title()}'s Total money: {players[player]['Money']}")

def player_lose(players, player):
  players[player]["Money"] -= players[player]["Bet"]
  print(f"{player.title()} is now down to ${players[player]['Money']}")

def player_win(players, player):
  players[player]["Money"] += players[player]["Bet"]
  print(f"{player.title()} is now up to ${players[player]['Money']}")

def print_player_and_dealer_hands(players, dealer):
  #os.system('cls')  
  for key in players:
    print(f"{key}'s hand is: {players[key]['Hand']}")
  print(f"Dealer's hand is: [{dealer['Hand'][0]}, ?]")

def play_hand(hand, decision):
  function = blackjackplayerchoices.choices[decision]
  while decision != "stay" :
    function(hand)
    if check_if_lose(hand):
      return False
    decision = input("Would you like to hit or stay: ").lower()
  return True

def check_if_lose(hand):
  sum = 0
  for num in hand:
      sum+=num
  return sum > 21

test_person = {
  "Name": "chad",
  "Money": 5000,
  "Hand": []
}

initial_give_cards(test_person["Hand"])
#play_blackjack(test_person)

print(test_person["Hand"][1])


  