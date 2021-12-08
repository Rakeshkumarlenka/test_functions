class Tup_creat():
    def __init__(self):
        self.t = ('hi', 55, 89, (12, 34, 'welcome'))
    def tuple_additem(self):
        l = list(self.t)
        l.append(1000)
        print(tuple(l))

result = Tup_creat()
result.tuple_additem()