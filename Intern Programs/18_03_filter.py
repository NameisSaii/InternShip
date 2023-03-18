def iseven(x):
    if x%2==0:
        return True
    else:
        return False
l=list(map(int,input().split()))
l1=list(filter(iseven,l))
print(l1)