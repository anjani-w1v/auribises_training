"""
    Read the file Session10B.py
    Analyze and count the objects in file
    Write the objects in a file named objectanalysis.csv or objectanalysis.txt
    Vehicle,5
    FastTag,5
    TollPlazaQueue,1
"""

objects = {
    'Vehicle': 0,
    'FastTag': 0,
    'TollPlazaQueue': 0
}

file = open('Session10B.py', 'r')
lines = file.readlines()

for line in lines:
    if "Vehicle(" in line:
        objects["Vehicle"] += 1

    if "FastTag(" in line:
        objects["FastTag"] += 1

    if "TollPlazaQueue(" in line:
        objects["TollPlazaQueue"] += 1


with open('objectanalysis.csv', 'a') as file:
    for key in objects:
        data = f'{key},{objects[key]}\n'
        file.write(data)



# count=0
    # if object:
    #     count=+1
    # print(count)

# file = open('objectanalysis.txt', 'w')
# write=input('Enter: ')
