class List_problems():
    def add_ele(self):
        print("")
        print("Q47.INSERT AN ELEMENT BEFORE EACH ELEMENT OF A LIST")
        color = ['Ram', 'Girish', 'Bobby','hari','sriya']
        print("Original List: ", color)
        color = [v for ele in color for v in ('H', ele)]
        print("NEW List: ", color)

res = List_problems()
res.add_ele()