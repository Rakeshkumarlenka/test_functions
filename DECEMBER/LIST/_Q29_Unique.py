#Get unique values
class List_problems():
    def unique(self):
        print("")
        print("Q29.GET UNIQUE VALUES")
        in_list=[1,  1, 1, 3, 4, 3, 3, 5,9,66,8]
        list_set = set(in_list)
        unique_list = (list(list_set))
        for x in unique_list:
            print (x)

res = List_problems()
res.unique()




