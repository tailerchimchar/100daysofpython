'''
Rock = 0
Paper = 1
Scissors = 2
'''
def returnWinner(player1, player2):
  if(player1 == player2):
    return "It is a draw."
  elif(player1 == 0): # player chose rock
    if(player2 == 1):
      return "You are defeated!"  
    else: 
      return "Rock beats scissors! You win!" 
  elif(player1 == 1): # player chose paper
    if(player2 == 0):
      return "Paper beats rock! You win!"
    else: 
      return "Scissors beats paper! You lose!"
  else: #player chose scissors
    if(player2 == 0):
      return "Rock beats scissors! You lose!"
    else:
      return "Scissors beats paper! You win!"