# Modifying global scope 
enemies = "Skeleton"

def increase_enemies():
  enemies = "Zombie"
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside: {enemies}")
# this prints skeleton \n zombie (why?) these two variables are entirely different

# to fix:
enemies = "Skeleton"
def increase_enemies():
  global enemies
  enemies = "Zombie"
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside: {enemies}")
# ^^ this is not recommended. don't use global. just use a return statement

def increase_enemies():
  print(f"Enemies inside function: {enemies}")
  return enemies + 1

#local scope 

# there is no block scope within python
game_level = 3

def create_enemy():
  enemies = ["Skeleton", "zombie", "alien"]
  if game_level < 5:
    new_enemy = enemies[0]
  print(new_enemy)
