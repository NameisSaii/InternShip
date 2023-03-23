a,b=list(map(int,input().split()))
s=lambda a,b: a if a>b else b
if s==a:
    print(a,"is bigger")
else:
    print(b,"is bigger")
