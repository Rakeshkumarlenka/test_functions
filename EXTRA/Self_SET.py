person1 = 'dress' , 'shoe' , 'bag'
print(set(person1))
person2 = 'shoe' , 'mobile', 'shop' ,'sampoo'
print(set(person2))


#add
a = {'shoe', 'dress', 'bag'}
a.add("trimmer")
print ("person1 item set is :",a)


#common item
a = {'shoe', 'dress', 'bag'}
y={'shoe', 'shop', 'sampoo', 'mobile'}
z = a.intersection(y)
print(z)

#combaine all iteam
j = {'shoe'}
k = {'dress', 'bag'}
l= {'trimmers','jacket'}
result = j.union(k,l)
print(result)


#remove
n={'dress', 'jacket', 'trimmers', 'bag', 'shoe'}
n.remove("jacket")
print(n)

#n.remove(99)    #KeyError: 99
n.discard(99)    #no error
print(n)

#delete random item from the set
n.pop()
print(n)

#check all item is present or not if present gave true or false
a = {'shoe', 'dress', 'bag'}
n={'dress', 'jacket', 'trimmers', 'bag', 'shoe'}
z = a.issubset(n)
print(z)

n={'dress', 'jacket', 'trimmers', 'bag', 'shoe'}
a = {'shoe', 'dress', 'bag'}
z = n.issuperset(a)
print(z)