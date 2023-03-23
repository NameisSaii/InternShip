"""
#while loop
x=1
while x<=10:
    print(x)
    x+=1
"""
"""
n=int(input("enter some number"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i+=1
print("The sum of first",n,"numbers is:",sum)
"""
"""
#for loop
for i in range(4):
    for j in range(4):
        print("i={} and j={}".format(i,j))
"""
"""
n=int(input("Enter the number of rows"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
n=int(input("Enter the number of rows:"))
for i in range(n):
    for j in range(i):
        print("*"*i)
    print()