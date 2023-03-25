#Bit wise operators
print(4&5)
print(4|5)
print(4^5)
print(~True)
print("Shift operators")
print(10<<2)
print(10>>2)
print("Assignment operators")
x=1
a,b,c=10,20,30
x+=a
print(x)
print("ternary operator")
a,b=4,5
x=30 if(a<b) else 40
print(x)
print("to find minimum value")
a=25
b=20
max=a if(a>b) else b
print(max)
print("Special operators 1.Identity operator(is,is not) 2.Member ship operator (id)")
#to compare the addresses we use identity operators
a=10
b=10
print(a is b)
l1=[1,2,3]
l2=[1,2,3]
print(id(l1))
print(id(l2))
print(l1 is l2)
print(l1==l2)