

from random import shuffle
lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)



class Shuff():
    def suf_ist(self):
            print("--------LIST IS---------------")
            print(lst)
            print("--------------------------------")
            shuffle(lst)
            print("----------*******---------------")
            print("After suffle list is :", lst)
            print("--------------------------------")
result = Shuff()
result.suf_ist()





