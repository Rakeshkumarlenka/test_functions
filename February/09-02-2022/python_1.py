'''
#Exercise 1: Print First 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i +=1

#Exercise 2: Print the following pattern
row = 5
for i in range(1,6,1):
    for j in range(1,i+1):
        print(j, end=' ')
    print(" ")


#Exercise 3: Calculate the sum of all numbers from 1 to a given number
#For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
#Enter number 10
# Sum is:  55

sum = 0
n = int(input('Enter the no :'))
for i in range(1,n,1):
    sum +=i
print('sum is ', sum)

#Exercise 4: Write a program to print multiplication table of a given number
n = 2
for i in range(1,11,1):
    prod = n * i
    print(prod)

#numbers = [12, 75, 150, 180, 145, 525, 50]
#output = 75 150 145

numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break
    elif i > 150:
        continue
    elif i % 5==0:
        print(i)

#Exercise 6: Count the total number of digits in a number

num = 32415
count = 0
while num != 0:
    num = num // 10
    count+=1
print("total digits are:",count)


#pattern

n = 5
row = 5
for i in range(0,6):
    for j in range(row-i,0,-1):
        print(j,end=' ')
    print()



#list1 = [10, 20, 30, 40, 50] reverse in vertical way

list1 = [10, 20, 30, 40, 50]
new = reversed(list1)
for i in new:
    print(i)
'''
#Display numbers from -10 to -1 using for loop(-10  to -1)
for i in range(-10,0,1):
    print(i)

#print 0 to 4 then done

for i in range(5):
    print(i)
else:
    print('Done')

#prime no for a range to print
'''
# range
start = 25
end = 50

Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47'''

start = 25
end = 50
for n in range(start, 51):
    if n > 1:
        for i in range(2,n):
            if (n % i )== 0:
                break
        else:
            print(n)




