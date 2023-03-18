"""
*-variable arguments
**-keyword arguments
keyword variable length arguments
"""
def display(**kwargs):
    print("Record information:")
    for k,v in kwargs.items():
        print(k,"..",v)
display(name="durga",marks=100)
display(name="ravi",wife='nandi')