#Recursin
#  def get_marks(numbers, length):
#     if length == 1:
#         return numbers[0]
#     else:
#         prev=
#         return get_marks(numbers, length-1)
    
# data=[11,22,33]
# print("max is:", get_marks(data,len(data)) )

# def search(*numbers, **number_to_search):
#     for number in numbers:
# #         print("[Log] comparing:", number with number_to_search)

# def sort(data):
#     for i in range(len(data)):
#         for j in range(len(data)-1-i):
#             print('i:', i, 'j:', j)
#             if data[j]>data[j+1]:
#                 data[j],data[j+1]=data[j+1],data[j]

  

# numbers = [10,30,40,5,15]
# sort(numbers)
# print("numbers:", numbers)

# ——————————————————————————# ——————————————————————————# ——————————————————————————# ——————————————————————————
#break every big problem to small and samll sub small parts to solve see below
"""
    data: [10, 20, 30]

    data: [10]             1 element
    if len(data) == 1
       max -> data[0]

       
    data: [10, 20]           2 element
    if len(data) == 1
       max -> data[0]
    else
        data[0] > data[1]
            return data[0]
        else
            returb data[1]

# """
# all elements

def get_max(numbers, length):
    
    if length == 1:
        return numbers[0]
    else:
        previous = get_max(numbers, length-1)
        current = numbers[length-1]
        
        if previous > current:
            return previous
        else:
            return current


# data = [10, 20, 30]
# data = [10]
data = [10, 40, 30, 50, 20]
result = get_max(data, len(data))
print('max is:', result)
#——————————————————————————————————————————————————————————————————————————————

# Product of Elements of a List with Recursion
# Draw the same in Stack

def product(numbers, length):
    if length == 0:
        return 1
    else:
        previous = product(numbers, length-1)
        current = numbers[length-1]
        return current * previous
        # return numbers[length-1] *  product(numbers, length-1)

data = [2, 3, 8]
result = product(data, len(data))
print('result is:', result)


