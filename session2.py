
# #instagram_user_name is a REFERENCE Variable
# instagram_user_name='auribises'    #Creational statement | Model         #stored in stack
# age = 30

# #output statement | View
# print('hashcode of instagram_user_name: ', id(instagram_user_name), type(instagram_user_name))
# print('hashcode of age: ', id(age), type(age))

# #data in right side - literal
# instagram_user_name='google'         #in this hashcode gets change
# johns_age = 30                       #in this hashcode remains same as of age


# print('hashcode of instagram_user_name:', id(instagram_user_name), type(instagram_user_name))
# print('hashcode of johns_age:', id(johns_age),  type(johns_age))

# del johns_age          #johns_age and age has same value so after del johns_age, age still point to 30
# #print('johns_age is:', johns_age)
# print('age is:', age)     #30
# del age
# print('age is:', age)            #NameError: name 'age' is not defined


#------------------------------------------------------------------------------------------------------

# creational statement + input
# age = int(input('Enter age: '))
# #output - view
# print('age is:', age, id(age), type(age))


# john_physics = 70
# john_chemistry = 80
# john_maths = 85

# fionna_physics = 75
# fionna_chemistry = 90
# fionna_maths = 95

# john_marks = [70, 80, 85]
# fionna_marks = [75, 90, 95]


#multivalue container

john_marks = [70, 80, 85, 'B', 'A','A']  #list- mutable .... str+int  so heterogenous. .... but always sure data in homogenous to perform any operatons
marks2 = [72, 88, 85]

class_marks=[        #list of lists
    [70, 80, 85],
    [72, 88, 85]
]


print('john_marks',  id(john_marks), type(john_marks))
print(len(john_marks))


print(john_marks[0], id(john_marks[0]), type(john_marks[0]))           #id- hashcode
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))
print(john_marks[2], id(john_marks[2]), type(john_marks[2]))
print(john_marks[3], id(john_marks[3]), type(john_marks[3]))
print(john_marks[4], id(john_marks[4]), type(john_marks[4]))
print(john_marks[5], id(john_marks[5]), type(john_marks[5]))         # both has same hashcode

john_marks[1] = 'B'
print(john_marks[1], id(john_marks[1]), type(john_marks[1]))

john_marks = 70, 80, 85    #can also write like this....tuple-immutable-u cannot modify data | READ ONLY
print(john_marks, id(john_marks), type(john_marks)) 
#john_marks[0] = 75        #tuple cannot modify so it gives error

