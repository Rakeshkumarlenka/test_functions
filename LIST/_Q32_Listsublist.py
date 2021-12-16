#Check a list contains sublist
class List_problems():
    def ch_sublist(self):
        print("")
        print("Q32.CHECK A LIST CONTAINS SUBLIST")
        test_list = [9, 4, 5, 8, 10]
        sub_list = [10, 5, 4]
        print("Original list : " + str(test_list))
        print("Original sub list : " + str(sub_list))
        flag = 0
        if (all(x in test_list for x in sub_list)):
            flag = 1
        if (flag):
            print("Yes, list is sublist of other.")
        else:
            print("No, list is not sublist of other.")

res = List_problems()
res.ch_sublist()