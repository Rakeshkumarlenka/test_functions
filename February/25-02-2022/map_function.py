def add(n):
    return n+n
numbers = (1,2,3,4,5)
result = map(add,numbers)
print(list(result))

#2
#Doube all number using map and lambda

numbers = (1,2,3,4,5,6)
result = map(lambda x: x + x, numbers)
print(list(result))

#3
#Add two list using map and lambda

lst1 = [1,3,5]
lst2 = [4,7,8,6]

result = map(lambda x,y: x + y,lst1,lst2)
print(list(result))


#4
#list of strings

lst = ['rak','reem','jas','mayu']
result = list(map(list, lst))
print(result)