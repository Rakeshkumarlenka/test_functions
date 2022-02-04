'''
#example for compile-time error
x=1
if x == 1
    print("where is colon?")

'''

'''
#runtime error
def concat(a,b):
    print(a+b)

concat('Hai',25)
'''
'''
#run time error
animal = ['dog','cat','horse','donkey']
print(animal[4])
'''
#logical errors
def increment(sal):
    sal = sal * 15/100
    return sal

sal = increment(5000.00)
print('incremented salary =%.2f' %sal)
'''

ERRORS:
-arithmetic Error
-Assertion error
-Attribute error
-EOFerror
-Floating point error
-GeneratorExit
-IOError
-Import error
-index error
-Key error
-KeyboardIntrupt
-Nameerror
-Not implimented error
-Overflow error
-runtime error
-stopIteration
-Syntax error
-Indentation error
-System Exit
-Type Error
-UnboundLocal error
-Value Error
-ZeroDivision error