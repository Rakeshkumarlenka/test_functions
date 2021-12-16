#Finding common items from two lists
class List_problems():
    def common_chek(self):
        print("")
        print("Q37.FINDING COMMON ITEMS FROM TWO LISTS")
        a = [1, 2, 3, 4, 5]
        b = [5, 1, 6, 7, 3]
        a_set = set(a)
        b_set = set(b)
        if (a_set & b_set):
            print(a_set & b_set)
        else:
            print("No common elements")

res = List_problems()
res.common_chek()


