class test:
    a=10
    def __init__(self):
        self.b=20
t1=test()
t2=test()
print(t1.a,t1.b)
print(t2.a,t2.b)
test.a=888#gets reflected on all varaibles
t1.b=999
print(t1.a,t1.b)
print(t2.a,t2.b)

"""
various places to declare static variables
1.within the class directly
class test:
    a=10
2.inside the constrctor using class name
    def __init__(self):
        self.b=20
        test.a=40
3.inside instance method by using class name
def m1(self):
    test.e=4
4.inside class method using class name or cls
  @classmethod
  def m2(cls):
  cls.f=60
  test.g=70
5 inside static method by using class name
 @staticmethod
 def m3():
    test.h=80
6.from oustside of class by using classname
  
  
  
"""
#how to access static variables
print("How to access static varaibles")
class test:
    a=10
    def __init__(self):
        print(self.a)
        print(test.a)
    def m1(self):
        print(self.a)
        print(test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(test.a)
        cls.f=60
        test.g=70
    @staticmethod
    def m3():
        print(test.a)
        test.h=80
t=test()
print(t.a)
t.m1()
t.m2()
t.m3()
print(test.a)