import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abaababa')
for match in matcher:
    count+=1
    print('match is available at start index',match.start())
print(count)
"""
finditer()
matcher=pattern.finditer('learning python is very easy')
1.start():start at the index of the match
2.end() end+1 index of the match
3.group -returns matched string

"""
pattern=re.compile('ab')
matcher=re.finditer('ab','abaababgdhaba')#another method
for m in matcher:
    count+=1
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))

print(count)
"""
 group()
 \s-space character
 \S except space character
 \d any digit
 \D except digits
"""
"""
a-> exactly one 'a'
a+-> atleeast one 'a'
a*-> ant number of a's including zero number also
a? -> atmost one a
eithe one a or zero number of a's
"""
"""
functions of re module
match()
fullmatch()
search()
findall()
finditer()
sub()
subn()
split()
compile
"""
