#
# lst = []
#
# n = int(input("Enter number of elements : "))
# for i in range(0, n):
#             ele = int(input())
#             lst.append(ele)
# print("--------LIST IS---------------")
# print(lst)
# print("--------------------------------")
# for i  in lst:
# 	if(i%2 == 0):
# 	    lst.remove(i)
#
# print("--------------------------------")
# print("--------------------------------")
# print ("list after removing EVEN numbers:",lst)


class Remo_eve():
    def even_re(self):
        for num in lst:
            if num % 2 != 0:
                print(num, end=" ")

lst = [2,4,5,6,7,8,10]
result = Remo_eve()
result.even_re()


