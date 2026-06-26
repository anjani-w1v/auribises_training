'''
#instagram_user_name is a REFERENCE Variable
instagram_user_name='auribises'    #CREATIoNAl statement | Model         #stored in stack
age = 30

#output statement | View
print('hashcode of instagram_user_name: ', id(instagram_user_name), type(instagram_user_name))
print('hashcode of age: ', id(age))

#data in right side - literal
instagram_user_name='google'
john_age = 30

del john_age
del age



#creational statement + input
age = int(input('Enter age: '))
#output - view
print('age is:', age, id(age), type(age))

'''

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



john_marks = 70, 80, 85    #tuple-immutable-u cannot modify data | READ ONLY
print(john_marks, id(john_marks), type(john_marks)) 


#hejjjjj