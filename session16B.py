#decorator
'''
Why decorators are useful:
Decorators let you add behavior before or after a function without changing the function's code. They're commonly used for:

Logging
Authentication/authorization
Measuring execution time
Input validation
Caching
Retry logic
Rate limiting

This is one of Python's most powerful features because it allows you to reuse common functionality across many functions.
'''



'''
def place_order():
    print('[LOG]order processing started...')
    print('order placed....')
    print('[LOG]order processing finished...')

place_order()
'''

def logger(func):    #func receives the function that will be decorated.
    def wrapper():
        print('[LOG]order processing started...')
        func()
        print('[LOG]order processing finished...')
    
    return wrapper

@logger
def place_order():
    print('[LOG]order processing successfully...')

place_order()      # or place_order = logger(place_order)

