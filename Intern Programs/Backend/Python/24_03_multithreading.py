#in ms word have sub process.. when you break down big task into parts is called thread
"""
if you want do multiple tasks
evry application have multiple threads

"""
"""
class hello:
    def run(self):
        for i in range(5):
            print("hello")

class hi:
    def run(self):
        for i in range(5):
            print("hi")
t1=hello()
t2=hi()
t1.run()
t2.run()
"""
#it execute first hello five times and then hi five times
#is there possibility to execute these two functions simultaneously
#that is multithreading
from threading import*
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(5):

            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1 )
t1=hello()
t2=hi()
#t1.run()
#t2.run()#even we're creating thread we're not getting output simultaneously
t1.start()
t2.start()
t1.join()
t2.join()
print("Bye")
