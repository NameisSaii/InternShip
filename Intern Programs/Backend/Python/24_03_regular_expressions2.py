import re
s=input("Enter the pattern to check")
m=re.search(s,'ababababab')
if m!=None:
    print("match is avilable")
    print("first occurence with start index:{} and end index{}".format(m.start(),m.end()))
else:
    print("full strring not matched")