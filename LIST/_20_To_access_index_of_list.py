lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")
print("Original list is : " + str(lst))
print("--------------------------------")
print("--------------------------------")
print("List index-value are : ")
print("----------*******************-----------")
class Inde_lis():
    def acc_in(self):
        for i in range(len(lst)):
            print(i, end=" ")
            print(lst[i])

result = Inde_lis()
result.acc_in()

print("--------------------------------")