#Mulitply of elements

lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

print("-----------********---------------------")


def multiplyList(lst):
    # Multiply elements one by one
    result = 1
    for x in lst:
        result = result * x
    return result

totalmult = multiplyList(lst);
print('multiplication of elements using function: ', totalmult)
print("--------------------------------")
print("-----------********---------------------")

class Multiply_Ele:
    def _init_(self,Multi):
        self.lst = Multi
    def pro_ele(self):
        pro = 1
        for n in lst:
            pro = pro*n
        print("Multiply of elements given a list using oops concept:",pro)

m = Multiply_Ele()
m.pro_ele()
print("-----------********---------------------")