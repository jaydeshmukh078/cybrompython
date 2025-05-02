# x=y=z=p=q=r=10  multiple variable single value assign
# x,y,z,p,q,r=1,2,3,4,5,6  multiple variable multiple value assign

x,y,z,p,q,r=10,10.5,10+10j,(1,2,3),'alfa',{1,'w',10} 
# multiple variable multiple Types value assign

print(x)
print(y)
print(z)
print(p)
print(q)
print(r)


# In built function


x=5
y=5
z=input("enter value :- ")
print(z)
print(id(x))
print(id(y))
print(x)
print(y)
print(type(x))
print(type(y))
print(x is y)#is that comparing address
print(x==y)