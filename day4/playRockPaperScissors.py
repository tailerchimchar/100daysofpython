import RockPaperScissors
import random
import RPPgamemechanics

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print('\nPlayer1 chose: ')
print(RockPaperScissors.game_elements[player_choice])

CPU_choice = random.randint(0,2)
print('\nCPU chose: ')
print(RockPaperScissors.game_elements[CPU_choice])

print(RPPgamemechanics.returnWinner(player_choice, CPU_choice))