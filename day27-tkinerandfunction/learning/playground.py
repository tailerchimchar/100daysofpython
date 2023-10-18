def add(*args):
  sum = 0
  for n in args:
    sum+=n
  return sum

print(add(3,5,8))
print(add(3,5))
print(add(1,2,3,4,5,6,7,8,9,10))

# unlimited keyword arguments
def calculate(n, **kwargs):
  print(kwargs)
  for key,value in kwargs.items():
    print(key)
    print(value)
    print(kwargs["add"])
    
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    
    print(n)
  
  
  
calculate(2, add=3, multiply=3)
# returns {'add': 3, 'multiply': 3}


class Car:
  def __init__(self, **kw):
    self.make = kw["make"]
    self.model = kw.get('model')
    
    # we want to use get because if it's not passed then it is okay
    
mycar = Car(make="Nissan", model = "gt-8")
print(mycar.model)