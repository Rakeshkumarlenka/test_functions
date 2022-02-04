#zip
#enumerate

list1 = [1,2,3]
list2 = ["a","b","c","d"]
zipped_list = list(zip(list1,list2))
print(zipped_list)
ennumerted_list = list(enumerate(list2))
print(ennumerted_list)

list1 = range(1,6)
list2 = range(11,16)
for i,j in zip(list1,list2):
    print(i," ",j)

func=lambda a: a*a
print(func(4))

name = "Rakesh"
a=(name.ljust(10))*3
print(a)
print(f"{name}\t"*3)