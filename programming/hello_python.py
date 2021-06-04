#Day 4

age = "18"  #age = string
print(age)
print(type(age))
n_age = int(age)   #make string to int(정수)
print(n_age)    
print(type(n_age))  

'''
def say_hello():
    print("Hello! I'm kwanehee:)")
    print("Bye ;)")
say_hello() 
'''

Minho = "minho"
def say_hello(name="jack"):  #name 값이 없으면
    print("hello", name)     #jack을 주라는 의미

say_hello(Minho)
say_hello()

def plus(a, b):
    print(a + b)
plus(3, 400)

def minus(a, b=0):   #b가 없으면 0을 주라는 의미
    print(a - b)
minus(3, 5)

def p_plus(a, b):
    print (a + b)

def r_plus(a, b):
    return(a + b)

p_result = p_plus(2, 3)

r_result = r_plus(2, 3)

print(p_result, r_result)

def say_hello_a(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} you ate from {are_from} you like {fav_food}"


hello = say_hello_a(name="kwanhee", age= "18", are_from="korea" ,fav_food="neang men")
print(hello)





