"""
types of exceptions
1.predefined exceptions /in built exceptions
2.user defined exceptions/customized exceptions

1.predefined exceptions
the exceptions which are raised automatically by python whenever a praticular
event occurs
eg:print(10/0) Zero divison error
eg2:x=int("ten")// value error
2.User defined exceptions
which we define
"""
class tooyoung(Exception):
    def __int__(self,arg):
        self.msg=arg
class tooold(Exception):
    def __int__(self,arg):
        self.msg=arg
age=int(input("Enter the age"))
if age>60:
    raise tooyoung("Please wait")
elif age<18:
    raise tooold("you're not ready")
else:
    print("thanks for registration")