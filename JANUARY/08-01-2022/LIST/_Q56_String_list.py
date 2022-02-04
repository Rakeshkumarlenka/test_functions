# Convert a string to a list
class List_prob:
    def str_list(self):
        str1 = input("Enter your string here: ")
        res = []
        for i in str1.split(" "):
            print(i)
            res.append(i)
        print(res)

res = List_prob()
res.str_list()

