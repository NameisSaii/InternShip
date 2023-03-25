"""
import re,urllib
import urllib.request
u=urllib.request.urlopen('https://www.redbus.in/info/contactus')
text=u.read()
numbers=re.findall('[0-9][-][0-9]',str(text))
for n in numbers:
    print(n)"""
import re
s=input('Enter mail id:')
m=re.fullmatch('\w[a-zA-z0-9_.]*@[a-z0-9]+[.]com',s)
if m!=None:
    print("Valid mail id")
else:
    print("Invalid mail id")