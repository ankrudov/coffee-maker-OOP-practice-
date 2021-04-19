from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#creating an object from the moneymachine blueprint,#object of the coffeemaker class
Money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu_objct = Menu()


#on/off 
is_on = True
action = 0

#show the menu options
while is_on == True:
    options = menu_objct.get_items()
    choice = input(f"What would you like ({options}) ? ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        Money_machine.report()
        coffee_maker.report()
    else:
       drink = menu_objct.find_drink(choice)
       if coffee_maker.is_resource_sufficient(drink):
           cost = drink.cost
           print(f"the price is {cost}")
           payment = Money_machine.make_payment(cost)
           if payment:
               coffee_maker.make_coffee(drink)
           else:
               continue
           
    
