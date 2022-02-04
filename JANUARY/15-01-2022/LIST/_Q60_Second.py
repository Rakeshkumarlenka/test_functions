#Find a tuple, the smallest second index value from a list of tuples
class List_probs:
    def small_index(self):
        x = [(4, 1), (1, 2), (6, 0)]
        print(min(x, key=lambda n: (n[1], -n[0])))

res = List_probs()
res.small_index()