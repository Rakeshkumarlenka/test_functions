#Print a list of space-separated elements
class List_probs:
    def space_sep(self):
        num = [1, 2, 3, 4, 5]
        print(*num)

res = List_probs()
res.space_sep()