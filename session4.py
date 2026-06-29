#set have n indexing 
#in dict 
#dump -- frames.  frame belong to main 
#main -- main thread 
###########source code .py -- we caed it module
#iterate -- set list dict
#in list only -- we can use index



# ——————————————————————————

# numbers = {10, 20, 30, 40, 50, 10, 20}
numbers = [10, 20, 30, 40, 50, 10, 20]
print(numbers, type(numbers), id(numbers))
print(numbers[0])

data = set(numbers)              #we define set ike this  and we cannt access eement in set cz no indexing
print(data, type(data), id(data))
#print(data[0])               #TypeError: 'set' object is not subscriptable


# ——————————————————————————  


product = {
    'code': 101,
    'name': 'Ultraboost',
    'brand': 'Adidas',
    'price': 8000,
    'category': 'shoe'
}

print(product, type(product), id(product))
print(product['code'], type(product['code']), id(product['code']))
print(product['category'], type(product['category']), id(product['category']))
print(product['brand'], type(product['brand']), id(product['brand']))

shoe_name = 'Adidas'              #pint t that adidas abve cntainer n new frm cz its frmed aready
print(shoe_name, type(shoe_name), id(shoe_name))

product['price'] = 7000           #in this new cntainer wi formm and that 8k cntainer wi destry r deete

for key in product:         #key = kuchbhi
    print(key, product[key])

# ——————————————————————————  

"""
void main(){

}

int main(){
    
    return 0;
}
 
class MyApp{                        #java
    public static void main(String[] args){
    
    }
}

"""

# main is a function py
def main():                   #in py we can run prgram even withut main functin its autmaticay and if using main functin this is the syntax and aways mentin see below which is main functin 
    print('Hello World')
    print('this is from main function')


if __name__ == '__main__':  # see here must t d this if u use main functin manually
    main()

# print('Hello World')
# print('this is from main function')

















