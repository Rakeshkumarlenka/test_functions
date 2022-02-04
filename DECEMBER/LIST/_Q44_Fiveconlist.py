#Generate group of five consecutive numbers in a list
class List_problems():
    def con_list(self):
        print("")
        print("Q44.FIVE CONSECUTIVE NUMBER IN A LIST")
        in_lis = [[5 * i + j for j in range(1, 6)] for i in range(5)]
        print(in_lis)

res = List_problems()
res.con_list()