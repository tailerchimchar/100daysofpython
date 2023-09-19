import hangman_art
import guess_words
import random
import hangman_mechanics

#flow - chart -> 
'''
1. Make a guess word
2. Make the blanks 
3. Have user guess a letter
4. If letter is not in word, then stage1 increase all the way until stage6 occurs, then output you lose
5. If letter is in word, then fill in all instances until the length of the word is reached 
'''

print(hangman_art.logo + "\n\n")
answer = random.choice(guess_words.words_list)
user_answer = ""
for letter in range(len(answer)):
  if(letter == ' '):
    user_answer+=' '
  else:
    user_answer+="_ "
user_answer_arr = user_answer.split()

stage = 6
print(hangman_art.stages[stage])
guess = ''
guessed_letters = []

while hangman_mechanics.game_not_won(user_answer, answer) and stage > 0:
  guess = input("What letter would you like to guess? \n").lower()
  if guess in guessed_letters:
    print("You already guessed this letter dummy\n")
    continue
  guessed_letters.append(guess)

  if len(guess) > 1:
    print("Your guess is too long")
  else:
    if answer.__contains__(guess):
      user_answer = hangman_mechanics.change_string(user_answer_arr, guess, answer)
      print(f"Correct!")
    else:
      stage-=1
      print(f"Wrong. You lose a life :)")
      print(hangman_art.stages[stage])
  print(user_answer)
  print(f"\n{guessed_letters}")
  print('\n')

if hangman_mechanics.game_not_won(user_answer, answer):
  print(f"You lost, the word was {answer}! Better luck next time!")
else:
  print("Great job! You won! :)")

