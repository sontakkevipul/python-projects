
# Default Parameter

def add(a=10,b=20):
    return a+b

# print(add()) TypeError: add() missing 2 required positional arguments: 'a' and 'b'
print(add()) # 30
print(add(5,2)) # 7

def func(name, l=[]):
    l.append(name)
    return l
    
print(func(1,[]))
print(func(4,[1,2]))
print(func(6)) 


# 1. no return, no parameters
# 2. yes return, no parameters
# 3. no return, yes parameters
# 4. yes return, yes parameters
 
 
def multiply(a,b,c=5,d=7,f=3,g=2):
    print("this is a's value:",a)
    print("this is b's value:",b)
    print("this is c's value:",c)
    print("this is d's value:",d)
    print("this is f's value:",f)
    print("this is g's value:",g)
    return a*b 

print(multiply(4,5))
print(multiply(b=4,a=5,g=9,d=2,c=0,f=1))
 
# Arbitrary Functions

# 1. *args
def calc(*numbers): # *args -> tuple of values
    print(numbers)
    print(type(numbers))
    total = 0
    for i in numbers:
         total +=i
    return total

print(calc(1,2,3,4))     
print(calc(1,2,3,4,5,6,7,8))     

print("this", "is","working","but","byebye!!")
 
 
def extra_param(*values,remove=0,add=1):
    print(*values) 
    print(remove)
    print(add)
    
    
# extra_param(1,2,3,4,5)    TypeError: extra_param() missing 2 required keyword-only arguments: 'remove' and 'add'

extra_param(1,2,3,4,5,remove=9,add=8)


# 2. **kwargs

def print_data(**values):
    print(values)
    print(type(values))
    for k,v in values.items():
        print(k, ":",v)
        
        
print_data(name="Harshit", roll_no = 101, age=30 ,marks=94, house="griffindor")        
print_data(name="Poornima", roll_no = 102 ,marks=94, house="Syllitherin")        
print_data(name="Vipul", age=30 ,marks=94, house="Hufflepuff")        
