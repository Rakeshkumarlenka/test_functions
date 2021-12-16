#Change the position of every nth value with (n+1)th value
from itertools import zip_longest, chain, tee
class List_problems():
    def ch_position(self):
        print("")
        print("Q38.CHENGE THE POSITION OF EVERY NTH VALUE WITH (n+1)th VALUE")
        lst = [0, 1, 2, 3, 4, 5]
        lst1, lst2 = tee(iter(lst), 2)
        print (list(chain.from_iterable(zip_longest(lst[1::2], lst[::2]))))

res = List_problems()
res.ch_position()




