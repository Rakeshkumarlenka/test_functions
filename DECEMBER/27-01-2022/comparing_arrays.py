#Q.Comparing two arrays and display the result in boolean type array
from numpy import *
a = array([1,2,3,0])
b = array([0,2,3,1])

c = a ==b
print("result of a==b :",c)
c = a >b
print("result of a > b :",c)
c =a <=b
print("result of a <= b :",c)


#program for to know the effects of any() and all() functions
from numpy import *
a = array([1,2,3,0])
b = array([0,2,3,1])
c = a >b
print("result of a > b :",c)

print("check if any one element is true :",any(c))
print("check if all elements are true : ",all(c))

if (any(a>b)):
    print("a contains atleast one element greater then those of b")


#program to understand the use of logical functions on arrays
