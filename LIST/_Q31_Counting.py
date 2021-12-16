#Counting number elementswithin a specified ranges
class List_problems():
    def count_range(self):
        print("")
        print("Q31.COUNTING NUMBER ELEMENTS A SPECIFIED RANGES")
        list1 = [10, 20, 30, 40, 50, 40, 40, 60, 70]
        l = 10
        r = 80
        c = 0
        for x in list1:
            if x >= l and x <= r:
                c += 1
        print(c)



res = List_problems()
res.count_range()