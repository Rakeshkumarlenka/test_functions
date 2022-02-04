# #Find common element from 2 lists
# list1 = []
# list2 = []
# num = int(input("Enter number of elements in list1: "))
# print("--------------------------------")
# print("----------*******---------------")
# for i in range(1, num + 1):
#     print("--------------------------------")
#     ele = int(input("Enter elements for list 2: "))
#     list1.append(ele)
# print("--------------------------------")
# print("----------*******---------------")
# print(list1)
# print("--------------------------------")
# print("--------------------------------")
# num = int(input("Enter number of elements in list2: "))
#
# for i in range(1, num + 1):
#     print("--------------------------------")
#     ele = int(input("Enter elements for list2: "))
#     list2.append(ele)
# print("--------------------------------")
# print("----------*******---------------")
# print(list2)
# def common(list1, list2):
#     return list(set(list1) & set(list2))
# e=common(list1,list2)
# print("--------------------------------")
# print("----------*******---------------")
# print("Common elements of two list is:",e)
# print("--------------------------------")

class Finder():
    def comm_ele(self,a,b):
        a_set = set(a)
        b_set = set(b)
        if (a_set & b_set):
            print(a_set & b_set)
        else:
            print("No common elements")

a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [8, 6, 5, 0]
result = Finder()
result.comm_ele(a,b)
