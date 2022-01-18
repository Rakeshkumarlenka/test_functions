
print('********************************************************************')
print("===============CREATE SET==============")
"""
1. Write a Python program to create a set.
"""

my_set = set()
my_second_set = {'a', 'b'}
print(my_set, type(my_set))
print(my_second_set, type(my_second_set))

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)

create()

print('********************************************************************')
print("===============ITERATE OVER SETS==============")
"""
2. Write a Python program to iterate over sets.
"""

my_set = {'a', 'b'}

for i in my_set:
    print(i)


print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    for i in a:
        print(i)

create()

print('********************************************************************')
print("===============ADD MEMBERS IN A SET==============")
"""
3. Write a Python program to add member(s) in a set.
"""

my_set = {'a', 'b'}
my_set.add('c')
print(my_set)


print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print("before adding new element")
    print(a)
    a2 = int(input("enter the new element"))
    a.add(a2)
    print("after adding new element")
    print(a)

create()

print('********************************************************************')
print("===============REMOVE ITEM FROM SET==============")
"""
4. Write a Python program to remove item(s) from set
"""

my_set = {'a', 'b'}
my_set.discard('a')
print(my_set)

my_set = {'a', 'b'}
my_set.remove('a')
print(my_set)

my_set = {'a', 'b'}
my_set.pop()
print(my_set)


print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print("before removing new element")
    print(a)
    a2 = int(input("enter the element to which to be removed"))
    a.remove(a2)
    print("after removing element")
    print(a)

create()


print('********************************************************************')
print("===============REMOVE ITEM FROM SET IF IT IS PRESENT ==============")
"""
5. Write a Python program to remove an item from a set if it is present in the set.
"""

my_set = {'a', 'b'}
my_set.discard('a')
my_set.discard('c')
print(my_set)


print('----**** USING FUNCTION ****-----------')

def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print("before removing new element")
    print(a)
    a2 = int(input("enter the element to which to be removed"))
    if a2 in a:
        a.discard(a2)
    else:
        print(a2, "is not available in the set so cant remove")
    print("after removing element")
    print(a)

create()


print('********************************************************************')
print("===============CREATE INTERSECTION OF SETS==============")
"""
6. Write a Python program to create an intersection of sets.
"""
set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.intersection(set_two)
set_inter2 = set_one & set_two

print(set_inter1)
print(set_inter2)

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    b = set()
    print("first set")
    a1 = int(input("how many values"))
    for i in range(a1):
        a2 = int(input("enter the elementss"))
        a.add(a2)
    print("second set")
    b1 = int(input("how many values"))
    for i in range(a1):
        b2 = int(input("enter the elementss"))
        b.add(b2)

    print(a.intersection(b))

create()



print('********************************************************************')
print("===============CREATE UNION OF SETS==============")
"""
7. Write a Python program to create a union of sets.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.union(set_two)
set_inter2 = set_one | set_two

print(set_inter1)
print(set_inter2)

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    b = set()
    print("first set")
    a1 = int(input("how many values"))
    for i in range(a1):
        a2 = int(input("enter the elementss"))
        a.add(a2)
    print("second set")
    b1 = int(input("how many values"))
    for i in range(a1):
        b2 = int(input("enter the elementss"))
        b.add(b2)

    print(a.union(b))

create()

print('********************************************************************')
print("===============CREATE SET DIFFERENCE==============")
"""
8. Write a Python program to create set difference.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.difference(set_two)
set_inter2 = set_one - set_two

print(set_inter1)
print(set_inter2)

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    b = set()
    print("first set")
    a1 = int(input("how many values"))
    for i in range(a1):
        a2 = int(input("enter the elementss"))
        a.add(a2)
    print("second set")
    b1 = int(input("how many values"))
    for i in range(a1):
        b2 = int(input("enter the elementss"))
        b.add(b2)

    print(a.difference(b))

create()

print('********************************************************************')
print("===============CREATE A SYMMETRIC DIFFERENCE==============")
"""
9. Write a Python program to create a symmetric difference.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'x', 'f'}

set_inter1 = set_one.symmetric_difference(set_two)
set_inter2 = set_one ^ set_two

print(set_inter1)
print(set_inter2)


print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    b = set()
    print("first set")
    a1 = int(input("how many values"))
    for i in range(a1):
        a2 = int(input("enter the elementss"))
        a.add(a2)
    print("second set")
    b1 = int(input("how many values"))
    for i in range(a1):
        b2 = int(input("enter the elementss"))
        b.add(b2)

    print(a.symmetric_difference(b))

create()


print('********************************************************************')
print("===============ISSUBSET AND ISSUPERSET==============")
"""
10. Write a Python program to issubset and issuperset.
"""

set_one = {'a', 'b', 'c'}
set_two = {'a', 'b'}

print(set_two.issubset(set_one))
print(set_one.issuperset(set_two))


print('----**** USING FUNCTION ****-----------')


def create():
    A = {1, 2, 3, 4, 5, 6}
    B = {1, 2, 3}
    print(A.issuperset(B))
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5, 6}
    print(A.issubset(B))

create()


print('********************************************************************')
print("===============CREATE SHALLOW COPY OF SETS==============")
"""
11. Write a Python program to create a shallow copy of sets. 
Note : Shallow copy is a bit-wise copy of an object. A new object is created
that has an exact copy of the values in the original object.
"""

set_one = {'a', 'b', 'c'}
set_two = set_one.copy()
print(set_one)
print(set_two)


print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    b = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)
    b = a.copy()
    print("after adding 10  20 and 30 to the set B")
    b.add(10)
    b.add(20)
    b.add(30)
    print(a)
    print(b)

create()


print('********************************************************************')
print("===============CLEAR A SET==============")
"""
12. Write a Python program to clear a set.
"""

set_one = {'a', 'b', 'c'}
set_one.clear()
print(set_one)

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)
    z = input("do you want to clear the set Y/N")
    z.lower()
    if z == "y":
        a.clear()
    print(a)

create()

print('********************************************************************')
print("===============USE OF FROZENSETS==============")
"""
13. Write a Python program to use of frozensets.
"""

set_one = frozenset((1, 2, 3))
set_two = set((1, 2, 3))
list_one = [4, 5, 6]
print (set_one == set_two)
print(set_one.isdisjoint(list_one))

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    fa = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)
    q = input("Do you want to freez the set Y/N")
    print("once you freez the set is immutabe")
    if q == "y":
        fa = frozenset(a)
    print(fa)

create()

print('********************************************************************')
print("===============MAXIMUM AND MINIMUM VALUE==============")
"""
14. Write a Python program to find maximum and the minimum value in a set.
"""

set_one = frozenset((1, 2, 3))
print(max(set_one))
print(min(set_one))

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)
    print("the maximum of the  above set is", max(a))
    print("the minimum of the  above set is", min(a))

create()

print('********************************************************************')
print("===============FIND THE LENGTH OF SET==============")
"""
15. Write a Python program to find the length of a set.
"""

set_one = frozenset((1, 2, 3))
print(len(set_one))
length = 0
for i in set_one:
    length += 1
print(length)

print('----**** USING FUNCTION ****-----------')


def create():
    a = set()
    a1 = int(input("how many values"))
    for i in range(a1):
        b1 = int(input("enter the elementss"))
        a.add(b1)
    print(a)
    print("the length of the set is", len(a))

create()

print('*******************************************************************')
