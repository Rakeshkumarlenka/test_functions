import itertools as it
def palindrome():
    #lst = []
    max_value = -1
    n = int(input("enter the number "))
    str_num = str(n)
    perm = it.permutations(str_num, len(str_num))
    for i in perm:
        str1 = "".join(i)
        if (str1 == str1[::-1]):
            if (int(str1) > max_value):
                max_value = int(str1)
    print(max_value)


palindrome()



# import itertools as it
# def palindrome():
#     lst = []
#     max_value = -1
#     n = int(input("enter the number "))
#     str_num = str(n)
#     perm = it.permutations(str_num, len(str_num))
#     for i in perm:
#         str1 = "".join(i)
#         if (i == i[::-1]):
#             lst.append(str1)
#             integer_map = map(int, lst)
#             integer_list = list(integer_map)
#             integer_list.sort()
#             max_va = integer_list[-1]
#             print("max",max_va)

