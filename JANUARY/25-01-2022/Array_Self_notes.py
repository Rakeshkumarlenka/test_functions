'''
ARRAYS ::
 -these are same as list but the diffrence was that arrays can store ony one type of elements, where as list can store diffrent types of elemnts
 -size of array is not fixed since we need not to specify how many elements we are going to store in an array in thr biggning
 - it can grow  or shrink in memory  dynamically(during run time)

'''

'''
Q1.Program to create an integer type array'''
import array
a = array.array('i',[2,3,4,5,8])
print("the array elements are ")
for element in a:
    print(element)


from array import *
a = array('i',[2,3,4,5,8])
print("the array elements are ")
for element in a:
    print(element)

'''Q.Create one arrary from another array'''
from array import *
arr = array('b',[2,3,4,5,8])

arr2 = array(arr.typecode,(a*3 for a in arr))
print("the array elements are ")
for element in arr2:
    print(element)

'''Elements of an array using index'''
from array import *
arr = array('i',[2,3,4,5,8])
n = len(arr)

for i in range(n):
    print(arr[i], end=' ')

print("-"*30)

from array import *
arr = array('i',[2,3,4,5,8])
n = len(arr)
i=0
while i<n:
    print(arr[i],end=' ')
    i+=1



'''Q.SLICING OF AN ARRAY'''
from array import *
x = array('i',[10,20,30,40,50,60,70,80])
for i in x[2:6]:
    print(i)


