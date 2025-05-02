''' day 1

import keyword
import string

#keywords...
print("1. KEYWORDS")
print("\n")

keys = keyword.kwlist
print("this is keywords")
print(keys)
print(len(keys))

softkeys = keyword.softkwlist
print("this is soft keywords")
print(softkeys)
print(len(softkeys))

#punctuation...
print("\n")
print("2. PUNCTUATION")
print("\n")

spesyb = string.punctuation
print("this is punctuation")
print(spesyb)
print(len(spesyb))

upper = string.ascii_uppercase
print("this is uppercase")
print(upper)
print(len(upper))

lower = string.ascii_lowercase
print("this is uppercase")
print(lower)
print(len(lower))







day 2


identifire....
rules



1. do not stsrt with digit (0-9)

0x=10
print(0x)


2. start with either letters (A-Z)(a-z) or underscore (_)

_x=10
print(_x)


3. do not use whitespace

_x y=10
print(_x y)


4. case-sensitive

x=10
print(X)


5. mix name 

xyz_abc01222=10
print(xyz_abc01222)






literals.......(constant value)

x=10
x=10.5
x='jay'
x=10+2

types of literls

1. numeric 
    1.1 int

x=10
print(x)
print(type(x))

    1.2 float

x=10.5555
print(x)
print(type(x))

    1.3 complex

x=2+10j
print(x)
print(type(x)) '''

# 2. string
#collection of charactor

# x='''nflcxv vzxfmzx;fmczdfvdsvsdmv
# dsklfmldsmfmzxlvmlsdf'''#multi line string
# y="beta"#single line string
# z='gama "beta" alfa'#single line string
# print(x)
# print(y)
# print(z)
# print(type(x))
# print(type(y))
# print(type(z))

# 3. list

# x=[1,2,'j','v']
# print(x)
# print(type(x))
# print(id(x))

# 4. tuple

# x=(1,2,'j','''v''')
# print(x)
# print(type(x))
# print(id(x))

# 5. dictionary

# x={'name':'jay','age':21,'qualification':'mca'}
# print(x)
# print(type(x))
# print(id(x))

# 6. set

# x={10,40,30,50,60,90,5,4,3,2,5,69,88,7,6,56,544444,}
# print(x)
# print(type(x))
# print(id(x))

# 7. frozenset

# fs={10,40,30,50,60,90,5,4,3,2,5,69,88,7,6,56,544444}
# x=frozenset(fs)
# print(x)
# print(type(x))
# print(id(x))