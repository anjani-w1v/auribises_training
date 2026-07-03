
# Search Operation: Linear Search O(n)
"""
def search(numbers, number_to_search):
    for number in numbers:
        print('[LOG] comparing:', number, 'with', number_to_search)
        if number == number_to_search:
            print('number found:', number)
            break
    else:
        print('Number Not Found')
search([10, 20, 30, 40, 50], int(input('Enter Number to Search ')))
"""

#———————————————————————————————————————————————————————————————————————————————————

#in this we * args appy to make it tupe so *numbers is nw tupe and in bew when call search gives errr 
# def search(*numbers, number_to_search):
#     for number in numbers:
#         print('[LOG] comparing:', number, 'with', number_to_search)
#         if number == number_to_search:
#             print('number found:', number)
#             break
#     else:
#         print('Number Not Found')


# search(10, 20, 30, 40, 50, int(input('Enter Number to Search ')))   #this gives errr cz number_to_search  becmes tupe so to avoid this we use kwargs** i.e why this will wrks in combination

#———————————————————————————————————————————————————————————————————————————————————
# def search(*numbers, **number_to_search):      #args *, kwargs**
#     for number in numbers:
#         print('[LOG] comparing:', number, 'with', number_to_search['key'])
#         if number == number_to_search['key']:
#             print('number found:', number)
#             break
#     else:
#         print('Number Not Found')


# search(10, 20, 30, 40, 50, key=int(input('Enter Number to Search ')))

#**number_to_search becmes dict key vaue pair


#———————————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————————
# https://visualgo.net/en/sorting
# Algo: Bubble Sort

def sort(data):
    for i in range(len(data)):
        for j in range(len(data) - 1 - i):
            print('[LOG] i:', i, 'j', j, '|' ,'data[j]', data[j], 'data[j+1]', data[j+1])
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]      #swap in py
                print('[LOG] >> SWAP: data[j]', data[j], 'data[j+1]', data[j+1])


numbers = [10, 30, 20, 5, 15]

"""
i: 0, 1, 2, 3, 4

i: 0
j: 0 1 2 3

i: 1
j: 0 1 2 

.
...
.......


"""

sort(numbers)
print("numbers:", numbers)

#———————————————————————————————————————————————————————————————————————————————————
#———————————————————————————————————————————————————————————————————————————————————
# Filter
# Linear Search Use Case
numbers = [10, 30, 20, 5, 15]

for number in numbers:
    # Filtering
    if number > 15:
        print(number)
