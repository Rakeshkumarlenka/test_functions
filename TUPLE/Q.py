
class Tup_remprob():
    def __init__(self):
        self.t = ('hi', 55, 89, (12, 34, 'welcome'), ['a', 'b', 'c'], True)

    def colon(self):
        my_tuple = (':',)
        my_colon = self.t
        print("------------Q8.COLON PROGRAM-------------")
        print(my_colon)
        print('-'*50)

    def repet_item(self):
        repeated_items = []
        my_tup = (1, 1, 2, 3, 4, 4, 5)
        for i in my_tup:
            if my_tup.count(i) > 1:
                repeated_items.append(i)
        print("------------Q9.REPETED ITEMS PROGRAM-------------")
        print(set(repeated_items))
        print('-' * 50)

    def check_ele(self):
        m = (1, 2, 4, 5,66,99)
        n = int(input("enter the no which you want to check :"))
        if n in m:
            print('presnt')
        else:
            print('not presnt')


result = Tup_remprob()
result.colon()
result.repet_item()
result.check_ele()












