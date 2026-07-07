'''
OOPS - object oriented programming

2 concepts-
object 
class

Principle of oops :
1. visualization = think of an object
2. draw/representation/textual represent the object
3. from the drawing/representatin create a real object

Real world
Object -> anything in exsitence eg: mango, AC, fan, human
class -> drawing/representatin of object(architectura Drawing/bueprint )
        Textual representation 

Cmputer Science wrd
Object -> strage cntainer(hmgenus/hetrgenus)
class -> Textual representation of object, how it will be in the memeory i.e. the 
'''

'''
Object -> instagram_account
Attributes -> mode, user, bio, email, email_address, phone_no., posts, videos

        ` posts
        ` likes, comments, shares,user

        `user 
        `name, phone,age, email, address[], gender, profile_image

1 user have many instagram_account

'''

class instagram_account:
    pass

class posts:
    pass

class user:
    pass


user1=user()           #these are nt bject these are reference variabes pointing in memry

user1.name='abcd'
user1.email='abc@gmail.com'
user1.gender='female'

user2=user()
user2.name='efgd'
user2.email='efg@gmail.com'
user2.gender='male'

user3=user()
user3.name='pqr'
user3.email='pqr@gmail.com'
user3.gender='female'


users=[user1, user2, user3]

instagram_account=instagram_account() 
instagram_account.mode='public'
instagram_account.username='hjy3454'
instagram_account.phone_no='+91 8456723454'
instagram_account.users=users

posts=posts()
posts.users='hjy3454'
posts.likes=10000


print('instagram_account:', instagram_account)
print('posts:', posts)
print('user1:', user1)
print('user2:', user2)
print('user3:', user3)

print('data in instagram_account:', vars(instagram_account))
print('data in posts:', vars(posts))
print('data in user1:', vars(user1))
print('data in user2:', vars(user2))
print('data in user3:', vars(user3))