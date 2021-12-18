import itertools
class List_problems():
    def rem_dup(self):
        print("")
        print("Q69.REMOVE DUPLICATES FROM LIST OF LISTS")
        num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
        print("Original List", num)
        num.sort()
        new_num = list(num for num, _ in itertools.groupby(num))
        print("New List", new_num)

res = List_problems()
res.rem_dup()