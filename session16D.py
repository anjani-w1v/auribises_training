#A lambda is simply an anonymous (unnamed) function assigned to a variable.

def compute_taxes(amount):
    return amount + 0.18*amount + 0.5*amount+1

taxes = lambda amount : amount + 0.18*amount + 0.5*amount+1

amount = 100

print(compute_taxes, type(compute_taxes))
print(taxes, type(taxes))

print(taxes(amount))

add = lambda a, b : a+b
print(add(10,20))

squares = lambda num : num*num
print(squares(25))