from array import *
arr = array('i',[10,20,30,40,50,60])
print("Original Array",arr)

arr.append(30)
arr.append(80)
print("After appending array is:",arr)

arr.insert(2,99)
print('After insert array is:',arr)

n = arr.pop()
print("After popping array is :",arr)
print("popped element is :",n)

n = arr.index(40)
print("index of 40 is :",n)

#convert an array to list using tolist() method
lst = arr.tolist()
print('List:',lst)
print("Array :",arr)