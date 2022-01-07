#Q1
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]
#myDict = {k: v for (k, v) in zip(keys, values)}
myDict = dict(zip(keys, values))
print(myDict)

#Q2
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

#Q3
sDict = {x.upper(): x*3 for x in 'coding '}
print (sDict)


#Q4
newdict = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(newdict)

#Q5
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)



#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)

#If Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)

#Q8
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)


#Q9
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)