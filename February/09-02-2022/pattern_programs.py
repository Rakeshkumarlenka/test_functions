#Q1
'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5'''

rows = 6
# if you want user to enter a number, uncomment the below line
# rows = int(input('Enter the number of rows'))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print(i, end=' ')
    # new line after each row
    print('')

#Q2
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5'''

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')

#Q3
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5'''

rows = 5
b = 0
# reverse for loop from 5 to 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print(b, end=' ')
    print('\r')

#Q4
'''
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5'''

rows = 5
num = rows
# reverse for loop
for i in range(rows, 0, -1):
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#Q5
'''
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1'''

rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i + 1):
        print(j, end=' ')
    print("\r")

#Q6
'''
1 
3 3 
5 5 5 
7 7 7 7 
9 9 9 9 9'''

rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print('')

#Q7
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1'''

rows = 5
# reverse loop
for i in range(rows, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")

#Q8
'''
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1'''

rows = 6
for i in range(1, rows):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print("")

#Q9
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1'''

rows = 5
for i in range(0, rows + 1):
    for j in range(rows - i, 0, -1):
        print(j, end=' ')
    print()

#Q10
'''
1
3 2
6 5 4
10 9 8 7'''

start = 1
stop = 2
current_num = stop
for row in range(2, 6):
    for col in range(start, stop):
        current_num -= 1
        print(current_num, end=' ')
    print("")
    start = stop
    stop += row
    current_num = stop



#Q11
'''
          1 
        1 2 
      1 2 3 
    1 2 3 4 
  1 2 3 4 5'''

rows = 6
for i in range(1, rows):
    num = 1
    for j in range(rows, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")


#Q12
'''
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1'''

def print_pascal_triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decide_number(i, j), end=" ")
        print()


def decide_number(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

# set rows
rows = 7
print_pascal_triangle(rows)



#Q13
'''
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5'''

rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

#Q14
'''
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64'''

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        square = i * j
        print(i * j, end='  ')
    print()

#Q15
'''
* 
* * 
* * * 
* * * * 
* * * * * '''

# number of rows
rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

#Q16
'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * '''



#answer 1-----
# number of rows
rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    # process each column
    for j in range(0, k):
        # print space in pyramid
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        # display star
        print("* ", end="")
    print("")

#Answer 2-----

rows = 5
for j in range(1, rows+1):
    print("* " * j)


#Q17
'''
* * * * *  
* * * *  
* * *  
* *  
*'''

rows = 5
for i in range(rows + 1, 0, -1):
    # nested reverse loop
    for j in range(0, i - 1):
        # display star
        print("*", end=' ')
    print(" ")

#Q18
'''
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             * '''

rows = 5
k = 2 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

#Q19
'''
*****
 ****
  ***
   **
    *'''

rows = 5
i = rows
while i >= 1:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i -= 1

#Q20
'''
            *   
           *  *   
          *  *  *   
         *  *  *  *   
        *  *  *  *  *   
       *  *  *  *  *  *   
      *  *  *  *  *  *  * '''

print("Print equilateral triangle Pyramid using asterisk symbol ")
# printing full Triangle pyramid using stars
size = 7
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=' ')
    print(" ")


#Q21
'''
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
* '''

rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print(" ")

print(" ")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")


#Q22
'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")


#Q23
'''
       * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        *'''



rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:
        # display space
        print(' ', end=' ')
        j += 1
    k = 1
    while k <= i:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(' ', end=' ')
        j += 1
    k = 1
    while k < i:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1


#Q24
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
    * 
   * * 
  * * * 
 * * * * 
* * * * *'''

rows = 5
i = 0
while i <= rows - 1:
    j = 0
    while j < i:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 1

i = rows - 1
while i >= 0:
    j = 0
    while j < i:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 1

#Q25
'''
****************
*******__*******
******____******
*****______*****
****________****
***__________***
**____________**
*______________*'''

rows = 14
print("*" * rows, end="\n")
i = (rows // 2) - 1
j = 2
while i != 0:
    while j <= (rows - 2):
        print("*" * i, end="")
        print("_" * j, end="")
        print("*" * i, end="\n")
        i = i - 1
        j = j + 2

#Q26
'''
        * 
       * * 
      * * * 
     * * * * 
    * * * * * 
   * * * * * * 
    * * * * * 
     * * * * 
      * * * 
       * * 
        * '''

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

k = rows - 2

for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

#Q27
'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *'''


rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1


#Q28
'''
A  
B C  
D E F  
G H I J  
K L M N O  
P Q R S T U  
V W X Y Z [ \ '''

# ASCII number of 'A'
ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")


#Q29
'''
P
Py
Pyt
Pyth
Pytho
Python'''

word = "Python"
x = ""
for i in word:
    x += i
    print(x)


#Q30
'''
            A  
           B C  
          D E F  
         G H I J  
        K L M N O  
       P Q R S T U  
      V W X Y Z [ \ '''

print("Print equilateral triangle Pyramid with characters ")
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")


#Q30
'''
V 
V V 
V V V 
V V V V 
V V V V V '''


# Same character pattern
character = 'V'
# convert char to ASCII
char_ascii_no = ord(character)
for i in range(0, 5):
    for j in range(0, i + 1):
        # Convert the ASCII value to the character
        user_char = chr(char_ascii_no)
        print(user_char, end=' ')
    print()


#Q31
'''
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
9 18 27 36 45 54 63 72 81 
10 20 30 40 50 60 70 80 90 100 '''



# Pyramid of horizontal tables of numbers
rows = 10
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(i * j, end=' ')
    print()



#Q32
'''
   1 
   2    1 
   4    2    1 
   8    4    2    1 
  16    8    4    2    1 
  32   16    8    4    2    1 
  64   32   16    8    4    2    1 
 128   64   32   16    8    4    2    1 '''


rows = 9
for i in range(1, rows):
    for j in range(-1 + i, -1, -1):
        print(format(2 ** j, "4d"), end=' ')
    print("")


#Q33
'''
   1 
   1    2    1 
   1    2    4    2    1 
   1    2    4    8    4    2    1 
   1    2    4    8   16    8    4    2    1 
   1    2    4    8   16   32   16    8    4    2    1 
   1    2    4    8   16   32   64   32   16    8    4    2    1 
   1    2    4    8   16   32   64  128   64   32   16    8    4    2    1 '''


rows = 9
for i in range(1, rows):
    for i in range(0, i, 1):
        print(format(2 ** i, "4d"), end=' ')
    for i in range(-1 + i, -1, -1):
        print(format(2 ** i, "4d"), end=' ')
    print("")


#Q34
'''
1 
2 3 4 
5 6 7 8 9'''


current_num = 1
stop = 2
rows = 3

for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 2



#Q35
'''
1 
2 3 
4 5 6 
7 8 9 10'''

current_num = 1
rows = 4
stop = 2
for i in range(rows):
    for column in range(1, stop):
        print(current_num, end=' ')
        current_num += 1
    print("")
    stop += 1


#Q36
'''
10 
10 8 
10 8 6 
10 8 6 4 
10 8 6 4 2'''


rows = 5
last_num = 2 * rows
even_num = last_num
for i in range(1, rows + 1):
    even_num = last_num
    for j in range(i):
        print(even_num, end=' ')
        even_num -= 2
    print("\r")


#Q37
'''
1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1'''


rows = 6
for i in range(1, rows + 1):
    for j in range(1, i - 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()

#Q38
'''
0  
0  1  
0  2  4  
0  3  6   9  
0  4  8   12  16  
0  5  10  15  20  25  
0  6  12  18  24  30  36'''


rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        print(i * j, end='  ')
    print()


#Q39
'''
1 2 3 4 5 
2 3 4 5 
3 4 5 
4 5 
5'''

rows = 5
for i in range(0, rows + 1, 1):
    for j in range(i + 1, rows + 1, 1):
        print(j, end=' ')
    print()


#Q40
'''
5 4 3 2 1 1 2 3 4 5 

5 4 3 2     2 3 4 5 

5 4 3         3 4 5 

5 4             4 5 

5                 5'''


rows = 6
for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print(j, '', end='')
    for l in range(i):
        print('    ', end='')
    for k in range(i + 1, rows):
        print(k, '', end='')
    print('\n')

#Q41
'''
1 * 2 * 3 * 4 

1 * 2 * 3 

1 * 2 

1'''

row = 4
for i in range(0, row):
    c = 1
    print(c, end=' ')
    for j in range(row - i - 1, 0, -1):
        print('*', end=' ')
        c = c + 1
        print(c, end=' ')
    print('\n')

#Q42
'''
0 
2 4 
4 8 8 
8 16 16 16'''

num = 4
counter = 0
for x in range(0, num):
    for y in range(0, x + 1):
        print(counter, end=" ")
        counter = 2 ** (x + 1)
    print()

