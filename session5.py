#model
#view - input print | cnse based
#controler -

#in singe vaue cntainer reference peratins is wrk diff
#++, -- -> these is nt avaiabe in pythn
# interview ques: static & dynamic memry management
#operators - artithmetic : + - */ ** // %
#            assignment : =, +=, -=, *=, /=, **=, %=    
#            conditinal : >, <, >=, <=, ==, !=  (will always return either true or false )
#            membership : is, in, not in, is not    
#               
#           00001101  11110010 +1  11110011 11111100 00000011 +1 00000100 -4  --->    -13>>2 = -4

# number1=10
# number2=3
# result=number1+number2
# print("result:", result)

#Boolean: True/ False    capital



# ——————————————————————————
# ——————————————————————————

# Operators
# Arithmetic : + - * / ** // %
# cab_fare = 200
# gst_tax = 0.18
# amount_to_pay = cab_fare + cab_fare*gst_tax
# print('amount_to_pay:', amount_to_pay)

# number1 = 10
# number2 = 3
# # result = number1 / number2
# # result = number1 // number2
# # result = number1 % number2
# result = number1 ** number2
# print('result:', result)


# # Assigment Operators: =, +=, -=, *=, /=, **=, %=
# # ++, -- -> this is not available in python
# number1 = 10
# number1 += 20 # number1 = number1 + 20
# number1 += 1
# number1 -= 1

# number1 *= 2
# print("number1:", number1)
# number2 = number1

# number1 *= 2
# print(number1)
# print(number2)


# Conditional Operators -> will always return either true or false
# >, <, >=, <=, ==, !=

# Membership Operators 
# is, in, not in, is not

# Logical Operators
# and or not

# wallet_amount = 300
# cab_fare = 300

# print('can i book the cab?', (wallet_amount >= cab_fare))

# # Boolean : True/False
# # internt = True

# # print(cab_fare is not wallet_amount)
# # print(cab_fare is not wallet_amount)

# # # print(cab_fare == wallet_amount)
# # print(cab_fare != wallet_amount)

# # # Assignment -> == vs is

# # data = [10, 20, 30]
# # print(10 in data)
# # print(100 not in data)

# # internet = True
# # gps = False

# # print('can i navigate?', internet and gps)

# # email = 'admin@example.com'
# # password = 'admin123'

# # user_email = input('Enter Email to Login: ')
# # user_password = input('Enter Password to Login: ')

# # print('Login Success?', user_email == email and user_password == password)


# # Bitwise Operators &, |, ^
# number1 = 8                      # 1 0 0 0
# number2 = 4                      # 0 1 0 0
# result1 = number1 & number2      # 0 0 0 0
# result2 = number1 | number2      # 1 1 0 0
# result3 = number1 ^ number2      # 1 1 0 0

# print('result1:', result1)
# print('result2:', result2)
# print('result3:', result3)

# # Shift Operators >>, <<
# number3 = 8         # 0 0 0 0 1 0 0 0  -> 8
# number4 = 2         # 0 0 0 0 0 0 1 0  -> 8>>2 -> 2
# result4 = number3 >> number4 # 8 >> 2

#  # 0 0 0 0 1 0 0 0  << 2
#  # 0 0 1 0 0 0 0 0 -> 8 << 2 -> 32
# result5 = number3 << number4 # 8 << 2
# print('result5:', result5) # -> 32

# data = 12
# key = 2     
# send_data_to_fionna = data >> key  # 12/2power3(>>) wrk n even number ny 12/2power3(>>) is n << k = n × (2^k) = 12 << 2= 12 × (2²)= 12 × (2²)= 48
# print('send_data_to_fionna:', send_data_to_fionna)
# data_received_by_fionna = send_data_to_fionna << key
# print('data_received_by_fionna:', data_received_by_fionna)



# data = 11                       # 0 0 0 0 1 0 1 1
# result = data >> 3              # 0 0 0 0 0 0 0 1 ----- 0 1 1
# print('result:', result)        # 1

# print('~~~~~~~~~~~~~~~~~')

# data = -11
# result = data >> 3
# print('result:', result) 
# """

#  11:  0 0 0 0 1 0 1 1
# -11:  1 1 1 1 0 1 0 0  1s complement
#                   + 1  2s complement

# -11 >> 3

#      1 1 1 1 0 1 0 0 >> 3
#      _ _ _ 1 1 1 1 0 --- 1 0 0
#      1 1 1 1 1 1 1 0 --- 1 0 0
#      0 0 0 0 0 0 0 1
#                    1
#      0 0 0 0 0 0 1 0 -> -2
# """      

# data = -13
# result = data >> 2
# print('result:', result) 

# Assignment -> explore below
# AES, SHA-256 etc are the security algorithms 
# which uses shifts and bitwise operations




# Conditional Constructs
# if else
# if elif else
# nested if else

# https://peps.python.org/pep-0008/
# How to write effective code in python following standards

email = 'admin@example.com'
password = 'admin123'

user_email = input('Enter Email to Login: ')
user_password = input('Enter Password to Login: ')

# regular/simple if/else

if user_email == email and user_password == password:
    print('Login is Successful')
else:
    print('Invalid Credentials. Either email or password is incorrect')


# nested if/else
"""
if user_email == email:
    if user_password == password:
        print('Login Success')
    else:
        print('Login Failed: Invalid Password')
else:
    print('Login Failed: Invalid Email')
"""