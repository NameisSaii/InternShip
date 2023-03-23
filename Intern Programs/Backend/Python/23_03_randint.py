from random import *
for i in range(10):
    print(randint(100000,999999))
print("Program to generate six digit password with letters and words consecutively ")
for j in range(10):
    print(chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9),chr(randint(65,65+25)),randint(0,9))