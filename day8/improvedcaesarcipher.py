from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ask_user_input():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt. Type exit to exit\n").lower()
  if direction != "exit":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  else:
    text = ""
    shift = 0
  return direction, text, shift

def caesar(text, shift, direction):
  end_text = ""
  if direction == "decode":
      shift *= -1
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      end_text += alphabet[new_position]
    else: 
      end_text += letter
  print(f"The {direction}d text is {end_text}")

direction, text, shift = ask_user_input()
while direction.lower() != "exit":
  caesar(text, shift%26, direction)
  direction, text, shift = ask_user_input()
  