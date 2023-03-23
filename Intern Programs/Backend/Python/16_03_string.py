""" find , strip,rstrip"""
s=input()
sub=input()
flag=False
pos=-1
n=len(s)
count=0
while True:
    pos=s.find(sub,pos+1,n)
    if pos==-1:
        break
    count+=1
    print("Found at index ",pos)
    flag=True
if flag==False:
    print("not found")
print("the number of times sub string repeated:",count)