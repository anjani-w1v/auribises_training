#function-piece of logic which repeatedly repeated 
#*args and varaibe arguments
#kwargs keywrd arguments
def add_numbers(number1, number2):
    resut = number1+number2
    print("resut is: ", resut)

print(add_numbers)
print(id(add_numbers),type(add_numbers), hex(id(add_numbers)))

add_numbers(1,3)


