
"""
s=input("enter some string")
i=0
print("the characters at even positions")
while i<len(s):
    print(s[i],end='')
    i=i+2
print()
"""
s1=input()
s2=input()
output=''
i=j=0
while i<len(s1) or j<len(s2):
    if len(s1):
        output=output+s1[i]
        i=i+1
    if j<len(s2):
        output=output+s2[j]
        j=j+1
    print(output)
