'''TYPES OF ARRAYS::
=Single Dimensional Arrays: these are represents only one row or column of elements
                     Ex: m = array('i',[20,40,30,60,70])

=Multi-diamnsional arrays: it represents more then one row and one column of elements
                     Ex: m = array([[1,2,3,4],[5,3,4,5,66],[66,4,8,0]]) '''

#CREATING ARRAY USING ARRAY() FUNCTIONS
#NUMPY IN ARRAYS
#Q1.A program creating a array
import numpy
arr = numpy.array([10,20,30,40])
print(arr)

import numpy as np
arr = np.array([10,20,30,40])
print(arr)

from numpy import *
arr = array([10,20,30,40])
print(arr)

#creating a array of charecters
from numpy import *
arr = array(['R','A','K','E','S','H'])
print(arr)

#CREATING ARRAY USING linspace() FUNCTIONS
from numpy import *
a = linspace(0, 20, 5)   #start, stop, n=how many no u want to print
print('a = ',a)


#CREATING ARRAY USING LOGSPACE() FUNCTION

from numpy import *
a = logspace(1, 4, 5) #range  was 10 ^ 1 to 10 ^4 devide into 5 diffrent parts
n = len(a)
for i in range(n):
    print('%.1f' %a[i], end='  ')

#CREATING ARRAY USING ARANGE() FUNCTION
from numpy import *
a = arange(2, 11, 2)
print(a)


#CREATING ARRAY USING ZEROS() AND ONES() FUNCTION
from numpy import *
a = zeros(6,int)
print(a)

b = ones(6)
print(b)
