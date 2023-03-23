n=int(input("Enter the number to find fatorial"))
def fact(n):
    if n==0:
        result=1
    else:
        result=n*fact(n-1)
    return result
c=fact(n)
print(c)
