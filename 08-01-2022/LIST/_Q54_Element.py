# Concatenate elements of a list
class List_prob:
    def concat_ele(self):
        lst1 = [1, 2, 3, 5, 4, 6]
        lst2 = [10, 20, 30, 40, 50]
        for i in lst2:
            lst1.append(i)
        print(lst1)


res = List_prob()
res.concat_ele()

