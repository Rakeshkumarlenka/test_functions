#Exercise 1: Print First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

#Exercise 2: Print the following pattern
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5'''

print("Number Pattern ")
row = 5
for i in range(1, row + 1, 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

#Exercise 3: Calculate the sum of all numbers from 1 to a given number
'''Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)'''
s = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
    s += i
print("\n")
print("Sum is: ", s)

#Exercise 4: Write a program to print multiplication table of a given number

