import random
lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
            ele = int(input())
            lst.append(ele)
print("--------LIST IS---------------")
print("Original list is : " + str(lst))
print("--------------------------------")

rand_idx = random.randint(0, len(lst) - 1)
random_num = lst[rand_idx]
print("--------------------------------")
print("--------------------------------")
print("Random selected number is : " + str(random_num))
print("--------------------------------")

class Item():
    def ran_item(self):
        lst1 = [4, 9, 0, 2, 4, 5, 7, 8, 1]
        print("random no is using oops:",random.choice(lst1))


result = Item()
result.ran_item()



