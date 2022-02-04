#create a dictionary from two lists without losing duplicate values.
from collections import defaultdict
class Create:
    def cre_dict(self):
        name_list = ['ram', 'hari', 'shyam', 'rohan']
        id_list = [10, 28, 28, 37]
        temp = defaultdict(set)
        for c, i in zip(name_list, id_list):
            temp[c].add(i)
        print(temp)

res = Create()
res.cre_dict()