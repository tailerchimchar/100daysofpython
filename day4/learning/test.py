import random
import my_module

c = random.randint(1,10)
print(c)

print(my_module.pi)

random_float = random.random()
print(random_float) # between [0,1)

random_float = random.random()*5
print(random_float) # between [0,1)
