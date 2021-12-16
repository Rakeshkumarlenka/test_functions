#Create a list by concatenating a given list which range goes from 1 to n
class List_problems():
    def concanate(self):
        print("")
        print("Q35.CREATE A LIST BY CONCANATING A GIVEN LIST WHICH RANGE GOES FROM 1 TO n")
        my_list = ['p', 'q','r']
        n = 5
        new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in my_list]
        print(new_list)

res = List_problems()
res.concanate()