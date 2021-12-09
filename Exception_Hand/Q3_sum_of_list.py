#Sum of elements

lst = []
try:
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
        print(lst)
except ValueError as vl:
    print("Error occured",vl)
finally:
    print(lst)


