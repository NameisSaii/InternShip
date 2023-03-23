#read a grop of int values from the keyboard as cmd line arguments and print sum
from sys import argv
args=argv[1:]
sum=0
for x in args:
    n=int(x)
    sum+=n
print("the sum",sum)
#in terminal the command like as follows filename.py 100 200 300
