from numpy import *
arr = array([10, 20, 30.5, -40])
print("original array is :",arr)

#arethmatic operation
print("After adding 4:",arr+4)
print("After substract 4:",arr-4)
print("After multiplication 4:",arr*4)
print("After division 4:",arr/4)
print("After modulous 4:",arr%4)

#uaing arrays as expressions also
print("Expression value:",(arr+5)**2-10)

#math function
print("Sin values:",sin(arr))
print("Cos values:",cos(arr))
print("tan values:",tan(arr))
print("Biggest elements values:",max(arr))
print("smallest elements values:",min(arr))
print("Sum of all elements:",sum(arr))
print("Average of the elements:",mean(arr))


