# remove an item from a tuple

class Tuple_probs:
    def remove(self):
        my_tuple = (1, 2, 3, 4, 5)
        my_new_tuple = my_tuple[:my_tuple.index(3)] + my_tuple[my_tuple.index(3) + 1:]
        print(my_new_tuple)


res = Tuple_probs()
res.remove()