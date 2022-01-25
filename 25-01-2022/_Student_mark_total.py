'''Program for storing students marks into an array and finding total marks and percentage of marks '''
from array import *
lst = [int(i) for i in input('enter marks: ').split(',')]
marks = array('i',lst)
sum = 0
for x in marks:
    print (x)
    sum+=x
print('Total marks:',sum)

n = len(marks)
percent = sum/n
print ("percentage :",percent)


