lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)

print("-----------********---------------------")
print("-----------********---------------------")
print(" list was ",lst)
print("-----------********---------------------")
print("-----------********---------------------")

class Spec():
    def remove(self):
        del lst[pos]
        print(*lst)

pos = int(input("Enter the index where you want to delete : "))
result = Spec()
result.remove()
print("-----------********---------------------")
print("list was: ",lst)
print("-----------********---------------------")



