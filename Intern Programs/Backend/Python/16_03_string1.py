""" counting substrings in the given string"""
s='ababfdjvnbmaa'
print(s.count('a'))
print(s.count('a',18,len(s)))
s=s.replace("a","b")
""" a will replace with b"""
print(s)
"""
chageing case of a string
upper()//convertsall to upper
lower()//converts all into lower
swapcase//upper to lower..if it's lower..it's converts in to lower
title()//every word starting will be capitilized
captalize()//just stratign word in a string is capitalized
"""