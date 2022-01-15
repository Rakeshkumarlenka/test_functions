#Create a list of empty dictionaries
class List_probs:
    def empty_dict(self):
        n = 5
        l = [{} for _ in range(n)]
        print(l)

res = List_probs()
res.empty_dict()