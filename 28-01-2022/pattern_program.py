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

