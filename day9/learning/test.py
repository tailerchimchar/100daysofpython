programming_dictionary = {
  "Bug": "Error in program",
  "Function": "Piece of code you can call over and over.",
  "Loop": "action that does something repeatedly",
  123: "Numbers",
}

print(programming_dictionary["Bug"]) # error in program
print(programming_dictionary[123]) # Numbers

# adding new entry:
programming_dictionary["Test"] = "Adding in test"
print(programming_dictionary)

#creates empty dictionary
empty_dictionary = {}

#wipes dictionary: 
programming_dictionary = {} #good for game stats and such

#edit an item in a dictionary
# if not there it will add it
programming_dictionary["Bug"] = "Moth in cpu"

#loop through a dictionary
for thing in programming_dictionary:
  print(thing)
#prints Bug Function Loop (not good)

#loop through a dictionary
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

