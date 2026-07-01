#1assignment
"""
    Another Brick in the Wall

    customer - 13 bricks
    iteration 1     3
    john  1         
    jack  2
    iteration 2     6+3 = 9
    john  2
    jack  4
    iteration 3     9 + 3 + 1 => 13 
    john  3
    jack  6 -> 1


    Answer: Who placed the last brick and how many
    jack placed the last brick. qty: 1

"""

n = int(input("Enter number of bricks: "))

john = 1
jack = 2

while n > 0:

    # John's turn
    if n >= john:
        n -= john
        last_person = "John"
        last_qty = john
    else:
        last_person = "John"
        last_qty = n
        break

    # Jack's turn
    if n >= jack:
        n -= jack
        last_person = "Jack"
        last_qty = jack
    else:
        last_person = "Jack"
        last_qty = n
        break

    # Next iteration
    john += 1
    jack += 2

print(f"{last_person} placed the last brick.")
print("Quantity:", last_qty)


#2assignment

"""
BINGO  : Flat ₹100 OFF, Minimum Amount ₹200
GET500 : Flat ₹500 OFF, Minimum Amount ₹1000
JUMBO  : Flat ₹300 OFF, Minimum Amount ₹500
"""

amount_in_cart = int(input("Enter Amount: "))
promo_code = input("Enter Promo Code: ")

if promo_code == "BINGO":
    if amount_in_cart >= 200:
        amount_in_cart -= 100
        print("BINGO Applied!")
        print("Final Amount:", amount_in_cart)
    else:
        print("Minimum cart amount should be ₹200")

elif promo_code == "GET500":
    if amount_in_cart >= 1000:
        amount_in_cart -= 500
        print("GET500 Applied!")
        print("Final Amount:", amount_in_cart)
    else:
        print("Minimum cart amount should be ₹1000")

elif promo_code == "JUMBO":
    if amount_in_cart >= 500:
        amount_in_cart -= 300
        print("JUMBO Applied!")
        print("Final Amount:", amount_in_cart)
    else:
        print("Minimum cart amount should be ₹500")

else:
    print("Invalid Promo Code")



# # OR
# promo_codes = {
#     "BINGO": {
#         "minimum_amount": 200,
#         "discount": 100
#     },
#     "GET500": {
#         "minimum_amount": 1000,
#         "discount": 500
#     },
#     "JUMBO": {
#         "minimum_amount": 500,
#         "discount": 300
#     }
# }

# amount_in_cart = int(input("Enter Amount: "))
# promo_code = input("Enter Promo Code: ").upper()

# print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print("You Entered Amount:", amount_in_cart)
# print("You Entered Promo Code:", promo_code)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~")

# if promo_code in promo_codes:

#     promo_rule = promo_codes[promo_code]

#     if amount_in_cart >= promo_rule["minimum_amount"]:

#         amount_to_pay = amount_in_cart - promo_rule["discount"]

#         print("Promo Code Applied Successfully")
#         print("Discount: ₹", promo_rule["discount"])
#         print("Please Pay: ₹", amount_to_pay)

#     else:

#         extra = promo_rule["minimum_amount"] - amount_in_cart

#         print("Promo Code cannot be applied.")
#         print("Add items worth ₹", extra, "more.")

# else:

#     print("Invalid Promo Code")