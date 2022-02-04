#Create multiple list
class List_problems():
    def mul_list(self):
        print("")
        print("Q41.CREATE MULTIPLE LIST")
        obj = {}
        for i in range(1, 10):
            obj[str(i)] = []
        print(obj)

res = List_problems()
res.mul_list()