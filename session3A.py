# Single Value Container
a = 10
b = a  # Reference Copy Operation. a into b

# Multi Value Container
data = [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]      #we put data into numbers.  imagine memry represenatin
numbers = data # Reference Copy Operation       #nw whatsapp shw changes in both devices 
#                   .... in this step what happen in memery that numbers list have remved or delete and it now becme data list so whatever change in data or numbers list it change in data list only not in numbers list coz earliar numbers list not exist see eg below

print("a:", a, id(a))
print("b:", b, id(b))    #a: 10 4352904712. b: 10 4352904712
print("data:", data, id(data))
print('numbers:', numbers, id(numbers))   #data: [10, 20, 30, 40, 50] 4300507328  numbers: [10, 20, 30, 40, 50] 4300507328
#------------------------------------------------------

data[1]=200

print("data:", data, id(data))
print('numbers:', numbers, id(numbers))     #data: [10, 200, 30, 40, 50] 4364650688  numbers: [10, 200, 30, 40, 50] 4364650688

numbers[2] = 36

print("data:", data, id(data))
print('numbers:', numbers, id(numbers))    #data: [10, 200, 36, 40, 50] 4338043072.  numbers: [10, 200, 36, 40, 50] 4338043072




#task1---------------------------------------------------------



phone_whatsapp=['Hi', 'Hello']
laptop_whatsapp=['Hi', 'Hello', 'bye']

phone_whatsapp=laptop_whatsapp            #['Hi', 'Hello', 'bye']. ['Hi', 'Hello', 'bye']
print(phone_whatsapp)
print(laptop_whatsapp)

phone_whatsapp[1]='hh'      #['Hi', 'hh', 'bye']. ['Hi', 'hh', 'bye']
print(phone_whatsapp)
print(laptop_whatsapp)

laptop_whatsapp[1]='yup'         #['Hi', 'yup', 'bye']. ['Hi', 'yup', 'bye']
print(phone_whatsapp)
print(laptop_whatsapp)

laptop_whatsapp=phone_whatsapp            #['Hi', 'yup', 'bye']. ['Hi', 'yup', 'bye']
print(phone_whatsapp)
print(laptop_whatsapp)





