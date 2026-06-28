# in pythn we use snake case (all letters small and use underscre)

#hashing     
#stack(LIFO) technical - eg. any app when go and when return back back back eg whatsapp
#      non-technical - plates at wedding
#in python reference variabe  has no type but in c++ has  eg void pointer... eg py - first ist ta then set then integer then string etc
#example - whatsapp(different in phone &o laptop)



# Single Value Container
a = 10
b = 10

# Multi Value Container
data = [10, 20, 30, 40, 50]
numbers = [10, 20, 30, 40, 50]

print("a:", a, id(a))   #same hashcode
print("b:", b, id(b))   #same hashcode
#aways imagine hw these paced in memry 
print("data:", data, id(data))                #diff hashcode
print('numbers:', numbers, id(numbers))        #diff hashcode

print("[0]:", data[0], id(data[0]), numbers[0], id(numbers[0]))      #[0] 10 4346826248 10 4346826248    #real life eg tech - whatsapp in phone and laptop (diff device) but points to same data hashcode same
data[1] = 100      #when we have msg but we read in phone's whatsapp only and laptop's whatsapp doesnt shw that it has read to overcome this (one of the bug) we have reference variable see on session3A
 #                                           |
print(data)                         #        |
print(numbers)   #[10, 100, 30, 40, 50].  [10, 20, 30, 40, 50].  









# coupons = [
#     'restaurant_coupons': {
#         : {
            
#         }
#     }
# ]
# chat_message = [
    
# ]