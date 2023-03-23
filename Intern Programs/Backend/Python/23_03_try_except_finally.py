
"""
Various possible combinations of try except else finally blocks
1.try block compulsory we should write either except or finally block
2.except with ou try is invalid
3.finally without try is invalid
4.we can take multiple except blocks for the same try but we cannot take multiple else and finally blocks
5.else without except is invalid
6.try-except-else-finally order is important
7.we can take try-except -else-finally in try,except,else,finally blocks
Nesting of try-except-else-finally is possible

"""
try:
    print("Outer try block")
    try:
        print("Inner try block")
        print(10/0)
    except ZeroDivisionError:
        print("Inner except block")
    finally:
        print("Inner finally block")
except:
    print("Outer except block")
finally:
    print("Outer finally block")