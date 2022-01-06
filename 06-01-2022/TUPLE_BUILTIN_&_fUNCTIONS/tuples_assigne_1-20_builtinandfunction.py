print('********************************************************************')
print("===============CREATE TUPLE==============")
"""
1.Write a Python program to create a tuple.
"""

my_empty_tuple = ()
my_multiple_tuple_with_braktes = ('abc', 'bcd', 'xyz')
my_list = [1, 2, 3, 3, 4]
my_tuple_from_list = tuple(my_list)


print(my_empty_tuple, type(my_empty_tuple), '\n',
      my_multiple_tuple_with_braktes, type(my_multiple_tuple_with_braktes), '\n',
      my_tuple_from_list, type(my_tuple_from_list))


print('----**** USING FUNCTION ****-----------')


def create_tuple():
    t = ('hi', 55, 89, (12, 34, 'welcome'))
    print(t)

create_tuple()

print('********************************************************************')
print("------------------------------------------")
print("===============CREATE TUPLE WITH DATATYPES==============")
"""
2.Write a Python program to create a tuple with different data types.
"""

my_tuple = ('abc', 1, 4.56, ['a', 'b', 'c'], True)
print(my_tuple)

for i in my_tuple:
    print(i, 'type is', type(i))


print('----**** USING FUNCTION ****-----------')

def tuple_diff_datatype():
        in_tup = ( "rain","hari", 90.0, "233@#")
        print("different data type", in_tup)

tuple_diff_datatype()

print('********************************************************************')
print("------------------------------------------")
print("===============CREATE TUPLE WITH NUMBERS AND PRINT ITEM==============")
"""
3.Write a Python program to create a tuple with numbers and print one item.
"""
from random import randint
my_tuple = (1, 2, 3, 3, 4)
print(my_tuple[randint(0, len(my_tuple)-1)])


print('----**** USING FUNCTION ****-----------')

def tuple_num():
        t_num = (31,88, 50, 67, 89, 99)
        print("tuple:", t_num)
        print("one element from tuple: ", t_num[3])

tuple_num()

print('********************************************************************')
print("------------------------------------------")
print("===============UNPACK OF A TUPLE==============")

"""
4. Write a Python program to unpack a tuple in several variables.
"""
my_tuple = ('a', 'b')
var1, var2 = my_tuple
print(var1, var2)


print('----**** USING FUNCTION ****-----------')

def tuple_unpak():
        a = ("Rakesh", 26 )
        b = ("sam", 26)
        (name, age) = b
        print(f"name: {name} , age:{age} ")

tuple_unpak()


print('********************************************************************')
print("------------------------------------------")
print("===============ADD A ITEM IN TUPLE==============")

"""
5. Write a Python program to add an item in a tuple.
"""

my_tuple = ('a', 'b')
my_new_tuple = my_tuple + ('c',)

print(my_new_tuple)


print('----**** USING FUNCTION ****-----------')


def tuple_additem():
    t = ('hi', 55, 89, (12, 34, 'welcome'))
    l = list(t)
    l.append(1000)
    print(tuple(l))

tuple_additem()





print('********************************************************************')
print("------------------------------------------")
print("===============CONVERT TUPLE TO STRING==============")

"""
6. Write a Python program to convert a tuple to a string.
"""
my_tuple = ('a', 'b')
my_string = ''.join(my_tuple)
print(my_string)


print('----**** USING FUNCTION ****-----------')

def tuple_convertstr():
        tuple = ('h', 'i', 'w', 'e', 'l', 'c', 'o', 'm', 'e','t','o','w','o','r','l','d')
        str = " "
        for i in tuple:
            str += i
        print(str)


tuple_convertstr()



print('********************************************************************')
print("------------------------------------------")
print("===============4TH ELEMENT OF LIST OT TUPLE==============")

"""
7. Write a Python program to get the 4th element
and 4th element from last of a tuple.
"""

my_tuple = tuple('abcdefgh')
print(my_tuple)
print('4th element is', my_tuple[3])
print('4th to last element is', my_tuple[-4])


print('----**** USING FUNCTION ****-----------')

def tuple_convertstr():
        in_tuple = ('h', 'i', 'w', 'e', 'l', 'c', 'o', 'm', 'e','t','o','w','o','r','l','d')
        item = in_tuple[3]
        print(item)
        item1 = in_tuple[-4]
        print(item1)

tuple_convertstr()




print('********************************************************************')
print("------------------------------------------")
print("===============COLON OF TUPLE==============")

"""
8. Write a Python program to create the colon of a tuple.
"""

my_tuple = (':',)
my_colon, = my_tuple
print(my_colon)


print('----**** new one ****-----------')


from copy import deepcopy

tup_col = ('Hello',1,True,[])
print(tup_col)
print(type(tup_col)) # -> tuple
tup_col_crt = deepcopy(tup_col)
print(type(tup_col_crt))  # -> tuple
tup_col_crt[3].append(10)
print(tup_col_crt)
"""
The original elements before deep copying
1 2 [3, 5] 4
The new list of elements after deep copying
1 2 [7, 5] 4
The original elements after deep copying
1 2 [3, 5] 4
The original elements before shallow copying
1 2 [3, 5] 4
The original elements after shallow copying
1 2 [7, 5] 4 
"""



print('********************************************************************')
print("------------------------------------------")
print("===============FIND REPETED ITEMS==============")


"""
9. Write a Python program to find the repeated items of a tuple.
"""

my_tuple = (1, 1, 2, 3, 4, 4, 5)

repeated_items = []
for i in my_tuple:
    if my_tuple.count(i) > 1:
        repeated_items.append(i)
print(set(repeated_items))


print('----**** USING FUNCTION ****-----------')

def repeted():
        my_tuple = (1, 1, 2, 3, 4, 4, 5)

        repeated_items = []
        for i in my_tuple:
            if my_tuple.count(i) > 1:
                repeated_items.append(i)
        print(set(repeated_items))


repeted()



print('********************************************************************')
print("------------------------------------------")
print("===============ELEMENT EXIST OR NOT==============")

"""
10. Write a Python program to check whether an element exists within a tuple.
"""

my_tuple = (1, 2, 3, 4, 5)

if 2 in my_tuple:
    print('2 is in', my_tuple)
else:
    print('2 is NOT in', my_tuple)

if 6 in my_tuple:
    print('6 is in', my_tuple)
else:
    print('6 is NOT in', my_tuple)



print('----**** new one ****-----------')


tuple_1 = (1,2,2,3,3,4,5,6,6)
print("Original tuple:",tuple_1)
element = input("Enter element:")
if element.isdigit():
    element = int(element)
elif element.isalpha():
    element = element.capitalize()
for item in tuple_1:
    if element in tuple_1:
        print("It exists")
        break
    else:
        print("Not exists")
        break




print('********************************************************************')
print("------------------------------------------")
print("===============LIST TO TUPLE==============")


"""
11. Write a Python program to convert a list to a tuple.
"""

my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(my_tuple)


print('----**** USING FUNCTION ****-----------')

def list_tuple():
        my_list = [1, 2, 3, 4, 5]
        my_tuple = tuple(my_list)
        print(my_tuple)


list_tuple()

print('********************************************************************')
print("------------------------------------------")
print("===============REMOVE AN ITEM FROM TUPLE==============")

"""
12. Write a Python program to remove an item from a tuple.
"""

my_tuple = (1, 2, 3, 4, 5)
# to remove number 3
my_new_tuple = my_tuple[:my_tuple.index(3)] + my_tuple[my_tuple.index(3)+1:]
print(my_new_tuple)



print('----**** USING FUNCTION ****-----------')


def tuplepro():
    tuple1 = (1,2,3,4,5,6)
    print(tuple1)
    list1 = list(tuple1)
    list1.remove(2)
    tuple1 = tuple(list1)
    print("After Removing 2:",tuple1)

tuplepro()

print('********************************************************************')
print("------------------------------------------")
print("===============SLICE OF TUPLE==============")

"""
13. Write a Python program to slice a tuple.
"""

my_tuple = tuple('axbxcx')

print(my_tuple[::2])


print('----**** USING FUNCTION ****-----------')

def tup():
    tuple1 = (1,2,3,4,5,6)
    print(tuple1)
    print("Tuple Slicing:",tuple1[:3])
    print("Tuple Slicing:",tuple1[3:])

tup()    


print('********************************************************************')
print("------------------------------------------")
print("===============INDEX OF TUPLE==============")


"""
14. Write a Python program to find the index of an item of a tuple.
"""

my_tuple = ('a', 'b')
print(my_tuple.index('a'))

print('----**** USING FUNCTION ****-----------')


def index():
        my_tuple = ('a', 'b')
        print(my_tuple.index('a'))


index()


print('********************************************************************')
print("------------------------------------------")
print("===============LENGTH OF TUPLE==============")

"""
15. Write a Python program to find the length of a tuple.
"""

my_tuple = ('a', 'b')
print(len(my_tuple))

print('----**** USING FUNCTION ****-----------')


def length():
        my_tuple = ('a', 'b')
        print(len(my_tuple))


length()



print('********************************************************************')
print("------------------------------------------")
print("=============== TUPLE TO DICTONARY==============")

"""
16. Write a Python program to convert a tuple to a dictionary.
"""

my_tuple = ('a', 1, 'b', 2)

my_dict = {}
for i in range(0, len(my_tuple), 2):
    my_dict[my_tuple[i]] = my_tuple[i+1]
print(my_dict)


print('----**** USING FUNCTION ****-----------')

def convert():
        my_tuple = ('a', 1, 'b', 2)

        my_dict = {}
        for i in range(0, len(my_tuple), 2):
            my_dict[my_tuple[i]] = my_tuple[i + 1]
        print(my_dict)

convert()


print('********************************************************************')
print("------------------------------------------")
print("=============== UNZIP A LIST OF TUPLE ==============")

"""
17. Write a Python program to unzip a list of tuples into individual lists.
"""

my_list = [(1, 2), ('a', 'b'), (True, False)]
new_list = []
for i in my_list:
    new_list.append(list(i))
print(*new_list)



print('----**** USING FUNCTION ****-----------')



def unzip():
        my_list = [(1, 2), ('a', 'b'), (True, False)]
        new_list = []
        for i in my_list:
            new_list.append(list(i))
        print(*new_list)


unzip()



print('********************************************************************')
print("------------------------------------------")
print("=============== REVERSE OF TUPLE ==============")


"""
18. Write a Python program to reverse a tuple.
"""
my_tuple = (1, 2, 3, 4)
reversed_tuple = my_tuple[::-1]
print(reversed_tuple)



print('----**** USING FUNCTION ****-----------')

def reverse_tup():
        my_tuple = (1, 2, 3, 4)
        reversed_tuple = my_tuple[::-1]
        print(reversed_tuple)


reverse_tup()



print('********************************************************************')
print("------------------------------------------")
print("=============== CONVERT LIST OF TUPLE TO DICTONARY  ==============")

"""
19. Write a Python program to convert a list of tuples into a dictionary.
"""

# solution 1 for unique keys
my_list = [('a', 1), ('b', 2)]
my_dict = {i[0]:i[1] for i in my_list}
print(my_dict)


print('----**** USING FUNCTION ****-----------')

def convert_dic():
        my_list = [('a', 1), ('b', 2), ('a', 5)]
        my_dict = {}
        for i in my_list:
            my_dict.setdefault(i[0], []).append(i[1])
        print(my_dict)


convert_dic()



print('********************************************************************')
print("------------------------------------------")
print("===============TUPLE WITH STRING FORMATION ==============")

"""
20. Write a Python program to print a tuple with string formatting.
Sample tuple : (100, 200, 300)
Output : This is a tuple (100, 200, 300)
"""

my_tuple = (100, 200, 300)
print('This is a tuple {}'.format(my_tuple))


print('----**** USING FUNCTION ****-----------')

def tup_str():
        my_tuple = (100, 200, 300)
        print('This is a tuple {}'.format(my_tuple))


tup_str()
