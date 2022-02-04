#Generate all sublists
class List_problems():
    def genrate(self):
        print("")
        print("Q33.GENERATE ALL SUBLISTS ")
        l = [1, 2, 3, 4]
        lists = [[]]
        for i in range(len(l) + 1):
            for j in range(i):
                lists.append(l[j: i])
        print( lists)

res = List_problems()
res.genrate()




