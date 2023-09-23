import blackjackmechanics
import random
bj_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def hit(hand):
  card_to_add = random.choice(bj_deck)
  if card_to_add == 11:
    sum = blackjackmechanics.calculate_total(hand) + 11
    if sum > 21:
      card_to_add = 1
  hand.append(card_to_add)
  print(f"Your hand is now {hand}")
  return 

def stay(hand):
  return

def split(hand):
  if hand[0] != hand[1]:
    return "Bust"
  else:
    hand1 = []
    hand1.append(hand[0])
    hand2 = []
    hand2.append(hand[1])
    print(f"{hand1}\n{hand2}")
    #hand 1 first
    decision = input("Would you like to hit or stay: ").lower()
    while(decision!= "stay"):
      hit(hand1)
      print(hand1)
      decision = input("Would you like to hit or stay: ").lower()
    while(decision!= "stay"):
      hit(hand2)
      print(hand2)
      decision = input("Would you like to hit or stay: ").lower()
  return


def double_down(hand):
  hand.append(random.choice(bj_deck))
  return

choices = {
  'Hit': hit,
  'Split': split,
  'Double Down': double_down,
  'Stay': stay,
}