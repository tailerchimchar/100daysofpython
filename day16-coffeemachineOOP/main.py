from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
atm = MoneyMachine()

order_name = input(f"What would you like? We have {menu.get_items()}: ").lower()
is_machine_on = False
if order_name != "off":
  is_machine_on = True
while is_machine_on:
  if order_name == "report":
    coffeemaker.report()
    atm.report()
  else:
    order = menu.find_drink(order_name)
    if coffeemaker.is_resource_sufficient(order):
      paid = atm.make_payment(order.cost)
      if paid:
        coffeemaker.make_coffee(order)
  order_name = input(f"What would you like? We have {menu.get_items()}: ")
  if order_name.lower() == "off":
    is_machine_on = False