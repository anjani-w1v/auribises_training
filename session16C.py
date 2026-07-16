class Burger:

    def __int__(self, name, price):
        self.name = name
        self.price = price
    
    def show(self):
        print('{name} | {price}'.format_map(vars(self)))

class MealDecorator:
    def __init_(self, burger):
        self.burger = burger
        self.burger.price += 100

    def show(self):
        self.burger.show()
        print('burger upgraded to meal with fries and coke')

burger1 = Burger(name = 'Noodles', price = 150)

