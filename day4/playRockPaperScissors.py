import RockPaperScissors
import random
import RPPgamemechanics

num_of_games = int(input("How many games do you want to play?\n"))
winner = ""
num_of_games_won = 0

for num in range(num_of_games):
  player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
  print('\nPlayer1 chose: ')
  print(RockPaperScissors.game_elements[player_choice])

  CPU_choice = random.randint(0,2)
  print('\nCPU chose: ')
  print(RockPaperScissors.game_elements[CPU_choice])
  winner = RPPgamemechanics.returnWinner(player_choice, CPU_choice)
  if winner.__contains__("You win!"):
    num_of_games_won+=1
  print(winner)

print(f"You won {num_of_games_won} games.")


