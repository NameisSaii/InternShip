v=['a','e','i','o','u']
d={}
word=input("Enter the word to find individual vowels count:")
for i in word:
    if i in v:
        d[i]=d.get(i,0)+1
for j,k in sorted(d.items()):
    print("{} repeated {} times".format(j,k))
