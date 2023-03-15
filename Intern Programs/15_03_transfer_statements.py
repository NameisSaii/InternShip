#transfer statements 1.break 2.continue 3.pass
#break is used to stop the current loop(based on some condition
#continue is used to stop the current iteration
#pass does nothing..to stop getting errors in current loop..
#for use future purpose we use pass
"""
cart=[100,200,2003,500,3044,56,88]
for item in cart:
    if item>500:
        print("sorry can't process order")
        break
"""
#continue
"""
for i in range(10):
    if i%2==0:
        continue
    print(i)
"""
for i in range(1,10):
    pass