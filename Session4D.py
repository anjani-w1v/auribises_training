data = [10, 20, 30, 40, 50]
# data = {10, 20, 30, 40, 50}
# print(data[0])
# print(data[1])
# print(data[2])
# print(data[3])
# print(data[4])

# Loop -> Iterate


for kuchbhi in data:         # For Each/ enhanced For loop(desnt give index)  # Read Only Loop
    print(kuchbhi)

# start from 0 go till 4 i.e. less than 5
# for index in range(0, 5):
# for index in range(0, len(data)):
# for index in range(len(data)):
for index in range(0,len(data),2):         #in list only we use this
    print(data[index])


for index in range(len(data)):
    data[index] = data[index]*2

print(data)


# while loop -> traditional loop
idx = 0
while idx < 5:
    print(data[idx])
    idx += 1

# ——————————————————————————


# for outer_index in range(0,5,1):
for outer_index in range(5):            # O(n) O(n*n)
    print(outer_index)
    print('-------------------')

    for inner_index in range(3):
        print(inner_index, end=' ')

    print('\n-------------------')

# if/else
# % division by 2 will give either 0 or 1



