import string
def game_not_won(user_answer, answer):
  return user_answer != answer

#change all occurrences of where guess is in answer
def change_string(arr, guess, answer):
  for num in range(len(arr)):
    if(guess == answer[num]):
      arr[num] = guess
  str = ""
  for letter in arr:
    str+=letter
  return str