#Find missing and additional values
class List_problems():
    def find_diff(self):
        print("")
        print("Q42.FIND MISSING AND ADDITIONAL VALUES")
        list1 = ['a', 'b', 'c', 'd', 'e', 'f','z','k']
        list2 = ['d', 'e', 'f', 'g', 'h']
        print('Missing values are: ', ','.join(set(list1).difference(list2)))
        print('Additional values were: ', ','.join(set(list2).difference(list1)))

res = List_problems()
res.find_diff()
