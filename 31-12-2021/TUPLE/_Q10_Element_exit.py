#Write a Python program to check whether an element exists within a tuple.
class Tuple_probs:
    def check(self):
        my_tuple = (1, 2, 3, 4, 5)

        if 2 in my_tuple:
            print('2 is in', my_tuple)
        else:
            print('2 is NOT in', my_tuple)

        if 6 in my_tuple:
            print('6 is in', my_tuple)
        else:
            print('6 is NOT in', my_tuple)


res = Tuple_probs()
res.check()