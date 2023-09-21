def greet():
  print('hello')
  print('how do u do')

# 2 parameters
def greet_with(name, location):
  print(f"Hello {name}")
  print(f"Hello {location}")

greet()

greet_with("Tailer", "nowhere")

greet_with(name="Tailer", location="London")

#same as
greet_with(location="london", name="tailer")