'''
File IO: file input utput stream 

# '''
# # file = open('session7C.py', 'r')
# file = open('/Users/anjani/auribisesTraining/a.txt', 'r')
# lines=file.readlines()
# file.close()
# print(type(lines), len(lines))

# # for line in lines:
# #     print(line)


with open('session11A.py') as file:
    lines=file.readlines()
    for line in lines:
        print(line)