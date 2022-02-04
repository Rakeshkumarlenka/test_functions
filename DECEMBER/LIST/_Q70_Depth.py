class List_problems():
    def depth_dict(self):
        print("")
        print("Q70.DEPTH OF A DICTONARY")
        dic = {1: 'rk', 2: {3: {4: {}}}}
        str_dic = str(dic)
        counter = 0
        for i in str_dic:
            if i == "{":
                counter += 1
        print (counter)


res = List_problems()
res.depth_dict()


