# Pythons Built In Module (JSON)
import json

order = {
    'oid': 1, 
    'customer': 'John',
    'dishes': 'dal, paneer, roti',
    'amount': 500
}

# print(type(order))
# print(order)

# Dictiory to JSON (String representation of Dictionary)
json_order = json.dumps(order)         #dump + s string

print(type(json_order))            #<class 'str'>       order dict ta but dumps cnvert it t text i.e string
print(json_order)         #gives in dict

# JSON to Dictiory (String converted to Dictionary)
order_dictionary = json.loads(json_order)
print(type(order_dictionary))        #<class 'dict'>
print(order_dictionary)         # dict