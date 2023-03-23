"""
Debugging means the complete control over the program execution.
 Developers use debugging to overcome program from any bad issues.
  So debugging is a healthier process for the program and keeps the diseases bugs far away.
  Python also allows developers to debug the programs using pdb module that comes with standard Python by default.
  We just need to import pdb module in the Python script. Using pdb module, we can set breakpoints in the program to check the current status.
  We can Change the flow of execution by using  jump,  continue statements
"""
import pdb

# It means , the Start of Debugging Mode
pdb.set_trace()

n = 5
for x in range(1, 11):
    print(n, '*', x, '=', n * x)