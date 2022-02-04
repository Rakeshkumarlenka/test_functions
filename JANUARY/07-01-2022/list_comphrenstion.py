#nested list
l = [10,20,30,40,[50,60]]
print("total list",l)
print("first element",l[0])
print("3rd element",l[3])
print("4th element",l[4])
for i in l[4]:
    print(i)

#list comprehensions
new = [x for x in l ]
print (new)


#Square list
square = [x**2 for x in range(1,11)]
print(square)

#Even or odd
obj = [f"{i} is Even" if i%2==0 else f"{i} is odd" for i  in range(20)]
print('\n'.join(obj))

obj = ["Even" if i%2==0 else "odd" for i  in range(20)]
print(obj)


#Skip element and print rest ele
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "Orange"]
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#upper case
newlist = [x.upper() for x in fruits]
print(newlist)
#print list all element below 5
in_list = [x for x in range(10) if x < 5]
print(in_list)

#replace all element with hello
newlist1 = [x if x != "banana" else "orange" for x in fruits]
print(newlist1)
newlist = ['hello' for x in fruits]
print(newlist)

