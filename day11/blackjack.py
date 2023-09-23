from art import logo
import blackjackmechanics
import blackjackplayerchoices
print(logo)

'''
1. Choose how many players are playing
1.5 Ask how much they're betting
2. Deal each player cards as well as the dealer has 1 card face down and 1 card face up (show it like [x, ?])
2.2 If player has 21 before the play phase then they win and earn double their amount 
2.5 If dealer has an Ace, then check bottom card and if it is 10 then instant win. 
3. Ask each player if they want to hit, stay, double down, split
4. If over 21, then they bust. 
5. if double down, then they only get 1 more card
6. If split, then it goes into 2 arrays and they can play blackjack for each hand 
7. If stand, then go on to next player
8. If hit, then add total to their card_amount
9. After last player plays, then reveal dealer
'''
num_players = int(input("How many players are playing?: "))
players = {}

def play():
  '''
  The play function that starts the game
  '''
  keep_playing = True
  same_players = False
  while keep_playing:
    # give players cards
    if same_players:
      hi = 000
    else:
      for count in range(num_players):
        blackjackmechanics.add_player(players, count)
    blackjackmechanics.give_players_cards(players)
    dealer = blackjackmechanics.deal_dealer()
    if blackjackmechanics.instant_blackjack(dealer):
      print('Unlucky')
    blackjackmechanics.print_player_and_dealer_hands(players, dealer)

    players_in = {}

    # hit, stay, double down, split
    if blackjackmechanics.instant_blackjack(dealer):
      for player in players:
        blackjackmechanics.player_lose(players, player)
    else:
      for player in players:
        current_hand = players[player]["Hand"]
        print(f"{player}'s current hand is {current_hand}")
        if players[player]["Already_Won"]:
          hello = "skipping this line"
        else:
          decision = input(f"Would {player.title()} like to 'Hit', 'Stay', 'Double Down', or 'Split'?: ").title()
        player_is_in = True
        if decision == "Double Down":
          players[player]["Bet"] *= 2
          blackjackplayerchoices.double_down(current_hand)
        elif decision!= "Stay":
          player_is_in = blackjackmechanics.play_hand(current_hand, decision)
        if player_is_in:
          players_in[player] ={
            "Name": players[player]["Name"],
            "Money": players[player]["Money"],
            "Hand": players[player]["Hand"],
            "Bet": players[player]["Bet"],
            "Already_Won": False,
          } 

          print("Nice! You make it to the next round.")
        else:
          print("Oops. You're out.")
          blackjackmechanics.player_lose(players, player)

    #input("Press enter when you're ready for the showdown...")
    blackjackmechanics.playersVsDealer(players_in, dealer)
    keepplaying = input("Want to keep playing? y or n: ")
    keep_playing = keepplaying == "y"
    # reset game:
    if keep_playing:
      same_players = True
      for player in players:
        players[player]["Hand"] = []

play()

