rec={}
n=int(input("Enter number of students"))
i=1
while i<=n:
    name=input("enter student name")
    marks=input("Enter marks:")
    rec[name]=marks
    i=i+1
for x in rec:
    print("\t",x,"\t\t",rec[x])

"""
 to update dictionary
 dict[key]=value
 d.clear()//all vlaues is erased..if you want add new values to d..it's possible
 del d//erased from memory
"""