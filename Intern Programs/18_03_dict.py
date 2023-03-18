""" take dictonary and print the sum of values"""
"""
d={1:200,2:200}
for j,l in d.items():
    print(j,l)"""
word=input()
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,v)