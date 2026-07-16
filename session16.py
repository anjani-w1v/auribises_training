orders = ['Pizza', 'Burger', 'Pasta', 'Noodles', 'Coke']
orders_iterator = iter(orders)

print(orders_iterator, type(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
print(next(orders_iterator))
#print(next(orders_iterator))       gives error StopIteration


#iterlist set tuple dict

order = 'Car'
for i in order:
    print(i)
print(order, type(order))


orderss = {
    'o1':'Pizza',
    'o2':'Pizza',
    'o3':'Pizza',
    'o4':'Pizza',
    'o5':'Pizza' 
}