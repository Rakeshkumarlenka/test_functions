"""
#Exercise 1: Accept numbers from a user
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

res = num1 * num2
print("Multiplication is", res)
"""
"""
#Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”
'''Use the print() function to format the given words in the mentioned format. Display the ** separator between each string.'''

print('My', 'Name', 'Is', 'James', sep='**')
"""
"""
#Exercise 3: Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

#Exercise 4: Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)
"""
"""
#Exercise 5: Accept a list of 5 float numbers as an input from the user
num = []
for i in range(0,5):
    print("Enter number at loaction",i,":")
    item = float(input())
    num.append(item)

print("user list:",num)

"""

#Exercise 6: Write all content of a given file into a new file by skipping line number 5
'''Create a test.txt file and add the below content to it.

Given test.txt file:               Expected Output: new_file.txt

line1                                  line1
line2                                  line2
line3                                  line3
line4                                  line4
line5                                  line6
line6                                  line7
line7

'''
'''
with open("test.txt","r") as fp:
    lines = fp.readlines()

with open("new_file.txt", "w") as fp:
    count = 0
    for line in lines:
        if count == 4:
            count +=1
            continue
        else:
            fp.write(line)
            count += 1

'''

#Exercise 7: Accept any three string from one input() call
'''Enter three string Emma Jessa Kelly
   Name1: Emma
   Name2: Jessa
   Name3: Kelly'''
"""
str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)
"""

"""
#Exercise 8: Format variables using a string.format() method.
#Write a program to use string.format() method to format the following three variables as per the expected output

# Given:                                                  Output:
# totalMoney = 1000                  I have 1000 dollars so I can buy 3 football for 450.00 dollars.
# quantity = 3
# price = 450

quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

"""
"""
#Exercise 9: Check file is empty or not
import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print('file is not empty')

"""
"""
#Exercise 10: Read line number 4 from the following file

with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])

"""