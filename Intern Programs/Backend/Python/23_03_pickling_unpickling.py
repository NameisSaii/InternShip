"""
pickle module implements a fundamental ,but powerful algorithm for serializing
and de-serializing a python object structre
'pickling' python object converted into byte stream(by using 'dump' function)
'unpickling' is inverse whereby a byte steam is converted back into object heirarchy(by using 'load' function)

"""
# this is pickling 
import pickle
list=["sai",'python']
with open("file.txt",'wb')as f:
    pickle.dump(list,f)

#unpickling
unpic=open("file.txt",'rb')
m=pickle.load(unpic)
print(m)