from resources import MENU, resources

decision = input("What would you like? (espresso, latte, cappuccino)").lower()

def calculate_cost(drink):
  cost = 0
  if decision == "cappuccino":
    cost = MENU[decision]["cost"]
  elif decision == "espresso":
    cost = MENU[decision]["cost"]
  elif decision == "latte":
    cost = MENU[decision]["cost"]
  else: 
    print("You did not enter a right drink.")
  return cost

def check_resources_sufficient(decision):
  sufficient_resources = True
  _ = 0
  required_ingredients = MENU[decision]["ingredients"]
  for item in MENU[decision]["ingredients"]:
    ingredient = item
    if resources[ingredient] >= required_ingredients[item]:
      _ = 1
    else: 
      print(f"You do not have enough {ingredient} to make {decision}")
      sufficient_resources = False
  return sufficient_resources

def make_drink(decision, cost):
  print(f"There is enough resources to make {decision}, making your drink.")
  cost = calculate_cost(decision)
  for item in MENU[decision]["ingredients"]:
    ingredient = item
    resources[ingredient] -= MENU[decision]["ingredients"][item]
  resources["money"]+=cost
  print(f"Adding {cost} to bank")

def report():
  print(resources)
  for resource in resources:
    if resource == "money":
      print(f"{resource}: ${resources[resource]}")
    else:
      print(f"{resource}: {resources[resource]}")

def coffeeshop():
  global decision
  while decision != "off":
    if decision == "report":
      print(report())
    else:
      cost = calculate_cost(decision)
      if check_resources_sufficient(decision):
        make_drink(decision, cost)
    decision = input("What would you like? (espresso, latte, cappuccino)").lower()
    if decision == "off":
      print("Machine closing down. Goodbye.")

coffeeshop()

  
  