"""
#Exercise 1: Calculate the multiplication and sum of two numbers
def mul_sum(a,b):
    mul = a * b
    if mul <=100:
        return mul
    else:
        return a +b

res = mul_sum(10,10)
print("the result is ",res)

res = mul_sum(10,20)
print("the result is ",res)

"""
"""
#Exercise 2: Print the sum of the current number and the previous number
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    previous_num = i
"""
'''
#Exercise 3: Print characters from a string that are present at an even index number
in_word = input('enter word')
print("original string:",in_word)

x = list(in_word)
for i in x[0::2]:
    print (i)

'''
'''
#Exercise 4: Remove first n characters from a string
def remove(word,n):
    print('Original String:', word)
    x =word[n:]
    return x

print("Removing characters from a string")
print(remove("welcome", 4))
print(remove("welcome", 2))
'''
'''
#Exercise 5: Check if the first and last number of a list is the same
def first_last_same(numberList):
    print("Given list:", numberList)
    first_num = numberList[0]
    last_num = numberList[-1]
    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

'''
'''
#Exercise 6: Display numbers divisible by 5 from a list
in_list = [10,20,33,46,55]
for i in in_list:
    if i % 5 == 0:
        print(i)
'''
'''
#Exercise 7: Return the count of a given substring from a string
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))
'''
'''
#Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for n in range(6):
    for i in range(n):
        print(n,end=" ")

    print('\n')
'''
'''
#Exercise 9: Check Palindrome Number
def palindrom(num):
    print("original number",num)
    original_num = num

    rev_num = 0
    while num > 0:
        rem = num % 10
        rev_num =(rev_num * 10) + rem
        num = num // 10

    if original_num == rev_num:
        print("Palindrom")
    else:
        print("not Palindrom")

palindrom(121)
palindrom(125)
'''

#Exercise 10: Create a new list from a two list using the following condition
'''Create a new list from a two list using the following condition
Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.
'''
'''
def merge_list(list1, list2):
    result_list = []
    for num in list1:
        if num % 2 != 0:
            result_list.append(num)

    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))

'''
'''
#Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#--If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

num = 7536
while num > 0:
    digit = num % 10
    num = num //10
    print(digit, end='')

'''
'''
#Exercise 12: Calculate income tax for the given income by adhering to the below rules

# Taxable Income	Rate (in %)
# First $10,000	  0
# Next $10,000	  10
# The remaining	  20
# 
# Expected Output:
# 
# For example, suppose the taxable income is 45000 the income tax payable is
# 
# 10000*0% + 10000*10%  + 25000*20% = $6000.

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

'''
'''
#Exercise 13: Print multiplication table form 1 to 10
for i in range (1,11):
    for j in range(1,11):
        print(i * j, end=" ")
    print("\t\t")
'''
'''
#Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(6, 0, -1):
    for j in range(0, i -1):
        print("*",end =' ')
    print(" ")
'''
'''
#Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)
'''