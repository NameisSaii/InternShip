l=[10,20,30,40,10,20,10,10]
target=int(input("Enter the value to search"))
try:
    print(target,"available first occurence is at ",l.index((target)))
except ValueError:
    print(target,"not available")

"""
append//appends the element in list
insert(index,element)//to add element at the specified position
extend()//if you want to add multiple elements at the en dof the list we use extend..if you
use append inplace of extend whole elements treated as list inside a list
"""