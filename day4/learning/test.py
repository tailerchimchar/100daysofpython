import random
import my_module

# random
c = random.randint(1,10)
print(c)

print(my_module.pi)

random_float = random.random()
print(random_float) # between [0,1)

random_float = random.random()*5
print(random_float) # between [0,5)

# Lists
states = ["Texas", "Delaware", "pennsylvania"]

states[0] #returns "Texas"
states[-1] #returns "Pennsylvania"

states[1] = "Dilloware" #changed to dilloware

states.append("TailerLand")

print(states) # prints 4 states

states.extend("Tailer", "Theresa")







