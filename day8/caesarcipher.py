import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# shift_letter would be easier if I just copy and pasted alphabet twice 
def shift_letter_encrypt(char, shift):
  index = alphabet.index(char)
  if char == ' ':
    return ' '
  elif(index + shift > 25):
    new_position = index + shift - 26
    return alphabet[new_position]
  else:
    return alphabet[index+shift]
  
def shift_letter_decrypt(char, shift):
  index = alphabet.index(char)
  if char == ' ':
    return ' '
  elif(index - shift < 0):
    new_position = index - shift + 26
    return alphabet[new_position]
  else:
    return alphabet[index-shift]


def shift_word_encrypt(word, shift):
  encrypted_word = []
  for num in range(len(word)):
    encrypted_word.append(shift_letter_encrypt(word[num], shift))
  print(f'The encoded text is {"".join(encrypted_word)}')

def encrypt(text, shift):
  text_arr = list(text)
  shift = shift % 26
  shift_word_encrypt(text_arr, shift)

def shift_word_decrypt(word, shift):
  decrypted_word = []
  for num in range(len(word)):
    decrypted_word.append(shift_letter_decrypt(word[num], shift))
  print(f'The decoded text is {"".join(decrypted_word)}')

def decrypt(text, shift):
  text_arr = list(text)
  shift = shift % 26
  shift_word_decrypt(text_arr, shift)

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

if direction.lower() == "encode":
  encrypt(text, shift)
elif direction.lower() == "decode":
  decrypt(text, shift)
else:
  print('Please write encode or decode')

