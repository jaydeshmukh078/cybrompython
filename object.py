# there are two types of object
# 1. immutable (structure not changable)
# 2. mutable (structure changable)

# x=10
# y=10

# print(id(x),id(y))

# x="jay"
# y="jay"

# print(id(x),id(y))

x=[2,3,4]
y=[2,3,4]

print(x,y)
print(id(x),id(y))

# --------------------------------------------------------------------------------------------------------------
# declaration of empty set (data type)
'''
# integer
print("integer")
x= int()
print(x)
print(type(x))

# float
print("float")
y= float()
print(y)
print(type(y))

# complex
print("complex")
z= complex()
print(z)
print(type(z)) '''


'''
data type    empty declaration  value
integer   -> int()            -> 0
float     -> float()          -> 0.0
complex   -> complex()        -> 0j
list      -> list()           -> []
string    -> str()            -> 
dictionry -> dict()           -> {}
dictionry -> dict()           -> {}
'''

# ---------------------------------------------------------------------------------------------------------------------
# type casting

# x=input("enter a number :- ")
# print(x)
# print(type(x))

# y = eval(input("enter a number :- "))
# print(y)
# print(type(y))

# ------------------------------------------------------------------------------------------------------------------------------



# in built function

# 1. print()
# 2. id()
# 3. min()
# 4. max()
# 5. type()
# 6. input()
# 7. eval()
# 8. sum()
# 9. len()
# 10. 


# s="python"
# print(sum(s))

# i=[10,20,30,40]
# print(sum(i))
# print(min(i))
# print(max(i))
# print(len(i))

# i=[10,20,30,'p']
# print(sum(i))  #error
# print(min(i))   #error
# print(max(i))   #error
# print(len(i))   

# in built class 

# 1. int str set 

# print("hello",end=',') #sep=' '  #inbuilt function attribute
# print("hi")

# x=10
# y=20
# print(x,y,sep='\n')  # end='\n'  #inbuilt function attribute


# import sys

# x=int()
# print("int : ",sys.getsizeof(x))
# y=float()
# print("float : ",sys.getsizeof(y))
# z=str()
# print("str : ",sys.getsizeof(z))
# p=list()
# print("list : ",sys.getsizeof(p))
# q=tuple()
# print("tuple : ",sys.getsizeof(q))
# r=dict()
# print("dict : ",sys.getsizeof(r))
# a=set()
# print("set : ",sys.getsizeof(a))
# b=frozenset()
# print("frozenset : ",sys.getsizeof(b))
