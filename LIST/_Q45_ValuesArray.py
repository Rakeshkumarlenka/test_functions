#Convert a pair of values into a sorted unique array

class List_problems():
    def value_arry(self):
        print("")
        print("Q45.CONVERT A PAIR OF VALUES IN TO A SORTED UNIQUE ARRAY")
        L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (8, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
        print("Original List: ", L)
        print("Sorted Unique Data:", sorted(set().union(*L)))

res = List_problems()
res.value_arry()