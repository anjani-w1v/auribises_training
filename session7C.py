# from session7B import flights
# # print(flights)

# # Sort on the fare, LOW to HIGH
# def sort(flights, low_to_high=True):
#     for i in range(len(flights)):
#         for j in range(len(flights) - 1 - i):

#             if low_to_high:
#                 if flights[j]['fare'] > flights[j+1]['fare']:     #ascending
#                 #if flights[j]['duration'] > flights[j+1]['duration']:     
#                 #if flights[j][key] > flights[j+1][key]:           see below after this ————————————
#                     flights[j], flights[j+1] = flights[j+1], flights[j]
#             else:
#                 if flights[j]['fare'] < flights[j+1]['fare']:      #descending
#                 #if flights[j]['duration'] < flights[j+1]['duration']:
#                 #if flights[j][key] < flights[j+1][key]:
#                     flights[j], flights[j+1] = flights[j+1], flights[j]


# #criteria = input('Enter Sorting Criteria: fare/duration: ')

# # sort(flights) same as sort(flights, low_to_high=True)

# sort(flights, low_to_high=False)

# for flight in flights:
#     print(flight)
#     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#———————————————————————————————————————————————————————————————————————————————————

#optimal way
from session7B import flights
# print(flights)

# Sort on the fare, LOW to HIGH
def sort(flights, key, low_to_high=True):
    for i in range(len(flights)):
        for j in range(len(flights) - 1 - i):

            if low_to_high:
                if flights[j][key] > flights[j+1][key]:
                    flights[j], flights[j+1] = flights[j+1], flights[j]
            else:
                if flights[j][key] < flights[j+1][key]:
                    flights[j], flights[j+1] = flights[j+1], flights[j]


criteria = input('Enter Sorting Criteria: fare/duration: ')

# sort(flights)
sort(flights, criteria, low_to_high=False)

for flight in flights:
    print(flight)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

