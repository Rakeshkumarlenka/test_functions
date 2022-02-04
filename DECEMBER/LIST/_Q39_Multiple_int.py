#Converting multiple integers into single integer
class List_problems():
    def mul_integer(self):
        print("")
        print("Q39.CONVERTING MULTIPLE INTEGERS INTO SINGLE INTEGER")
        L = [5,33,1,8]
        print("Original List: ", L)
        x = int("".join(map(str, L)))
        print("Single Integer: ", x)

res = List_problems()
res.mul_integer()

