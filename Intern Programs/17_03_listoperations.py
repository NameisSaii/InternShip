l=[20,0,15,10]
l.sort(reverse=True)
print(l)
""" 
copy operator clones..points to different memory location
== ->content comparison
is -> reference comparison
pop()//removes last element
pop(index)
x.clear()//removes x
list=[expression for x in sequence]
d.get(key)//you'll get the valuw which matched with the key
d.get(key,default)//if your not found you'll key the default value
d.pop(key)//removes that key
keys()
values()
items()
copy()//to create exact dictionary
setdefault(k,v)//if the key is already available..it returns the corresponding value
if it won't available it add that key value in to dictionary
"""
list=[x*x for x in range(1,11)]
print(list)
