"""
How to access characters from the string:
1.by using index
by using slice operator
"""
s='durga'
print(s[2])
print(s[1])
s=input("Enter the string")
i=0
for x in s:
    print("The character present at positve index:{} and at negative index:{}".format(i,i-len(s)))
    i=i+1