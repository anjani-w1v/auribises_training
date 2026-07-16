def delivery_orders():
    yield 'Pizza'
    yield 'Burger'
    yield 'Noodles'

menu = delivery_orders()
print(menu , type(menu ))      #<class 'generator'>

# print(next(orders))
# print(next(orders))
# print(next(orders))       #StopIteration error


for order in menu :
    print(order)

# #list
# def delivery_orders():
#     # yield 'Pizza'
#     # yield 'Burger'
#     # yield 'Noodles'
#     menu = ['Pizza', 'Burger', 'Noodles' ]

#     for item in menu :
#         yield item

# menu = delivery_orders()
# print(menu , type(menu ))      #<class 'generator'>

# # print(next(orders))
# # print(next(orders))
# # print(next(orders))       #StopIteration error


# for order in menu :
#     print(order)