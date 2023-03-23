"""
set operations
union-all elements combined
intersection-common
difference-
"""
s={10,20,30}
s.add(40)
print(s)
x=[1,2,34]
s.update(x)
print(s)
s2={20,40,60}
print(s.union(s2))
print(s.intersection(s2))
print(s.difference(s2))
