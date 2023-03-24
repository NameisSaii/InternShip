"""
class Employee:
    def __init__(self,eno,ename):
        self.eno=eno
        self.ename=ename
    def display(self):
        print("Employee no:",self.eno)
        print("Employee no:",self.ename)

e1=Employee(100,'durga')# here e1 is the reference variable
e2=Employee(200,'sai')
e1.display()
e2.display()
print(e1.__dict__)#to print instance varibles which related to that particular object
"""

"""
methods and
 .we can take any name in methods
 per object methods can be called any number of timees
 will be executed if we call that method
 inside method we can arite business logic
 constructors
1..but in constructors it shoud br __intit__
2.automatically when ever we are creating object
3.per object ,constructor will be executed only once
4.we have to decalre and intialize instance variables

"""
"""
Types of variables
1.instance variables(non-static)
( if the value of varables varies from object to object)
2.for every object a separate copy of intance variables will be created
3.in general inside constructor we have to declare by using self keyword
4.within the class by using self we access instance variables..but outside of class by using reference variables


2.static variables/class level varaibles
3.local variables

"""