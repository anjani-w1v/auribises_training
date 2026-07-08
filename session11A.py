# file = open('quotes.txt', 'w')
# file = open('quotes.txt', 'a')
# quote=input('Enter a quote: ')
# file.write(quote)
# file.close()

objects = {
    'Vehicle':0,
    'FastTag':0,
    'TollPlazaQueue':0,
}
file = open('session10B.py', 'r')
lines=file.readlines()
for line in lines:
    pass

    


with open('objectanalysis.txt', 'a') as file:
    for key in objects:
        data=f'{key},{objects[key]}\n'
        file.write(data)




    # count=0
    # if object:
    #     count=+1
    # print(count)

# file = open('objectanalysis.txt', 'w')
# write=input('Enter: ')
