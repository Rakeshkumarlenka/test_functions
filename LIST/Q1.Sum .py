#Sum of elements

lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print(lst)
print("--------------------------------")

total = 0
sum_of_list = 0

print("--------------------------------")
print("-----------****BUILT-IN METHODS*****---------------------")
sum_of_list = sum(lst)
print("sum of list using sum :",sum_of_list)
print("--------------------------------")

print("-----------****LOOP*****---------------------")
for ele in range(0, len(lst)):
    total = total + lst[ele]
print("-----------********---------------------")
print("Sum of all elements using loop: ", total)
print("-----------*********---------------------")

print("--------------------------------")


print("-----------****FUNCTIONS*****---------------------")
def listsum(lst):
    total = 0
    i = 0
    while i < len(lst):
        total = total + lst[i]
        i = i + 1
    return total

totalsum = listsum(lst);
print('Sum of List using function: ', totalsum)

print("-----------*********---------------------")
print("-----------****OOPS*****-----------------")
class Numbers:
    def __init__(self):
       self.__sum=0
    def addNumber(self, number):
       self.__sum += number
    def currentSum(self):
       return self.__sum

numbers = Numbers()
for n in lst:
        numbers.addNumber(int(n))
print("sum of list using oops:",numbers.currentSum())