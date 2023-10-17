# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas

data = pandas.read_csv("./nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#print(phonetic_dict)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Input a name: ").upper()

phonetic_code_word_list = [phonetic_dict[letter] for letter in name]
print(phonetic_code_word_list)
