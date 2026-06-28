# Creating Multi Value Containers (Data Structures)

# ref_var = () # Tuple
# ref_var = [] # List
# ref_var = {} # Dictionary not set

#for set
# ref_var = set()
#also
# ref_var = tuple()
# ref_var = list()
ref_var = dict()

print(ref_var, type(ref_var))


#---------------------------------------------------------


menu = {
    101: {
        'name': 'Dal Makhani',
        'price': 100
    },

    201: {
        'name': 'Paneer Butter Masala',
        'price': 300
    },

    301: {
        'name': 'Burger',
        'price': 120
    },

    401: {
        'name': 'Noodles',
        'price': 200
    },

    501: {
        'name': 'Mojto',
        'price': 80
    }
}

# print(menu)
print('---MENU----')

print('---------------------')
print(menu[101]['name'], '\t \u20b9', menu[101]['price'])
print('---------------------\n')

print('---------------------')
print(menu[201]['name'], '\t \u20b9', menu[101]['price'])
print('---------------------\n')

print('---------------------')
print(menu[301]['name'], '\t \u20b9', menu[101]['price'])
print('---------------------\n')

print('---------------------')
print(menu[401]['name'], '\t \u20b9', menu[101]['price'])
print('---------------------\n')

print('---------------------')
print(menu[501]['name'], '\t \u20b9', menu[101]['price'])
print('---------------------\n')

print('----------')




