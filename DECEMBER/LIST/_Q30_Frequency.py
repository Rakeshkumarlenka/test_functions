#Frequency of elements
class List_problems():
    def frequency(self):
        print("")
        print("Q30.FREQUENCY OF ELEMENTS")
        my_list = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
        freq = {}
        for item in my_list:
            if (item in freq):
                freq[item] += 1
            else:
                freq[item] = 1

        for key, value in freq.items():
            print("% d : % d" % (key, value))



res = List_problems()
res.frequency()