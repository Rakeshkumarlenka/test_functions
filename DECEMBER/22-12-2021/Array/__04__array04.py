from array import *
class Array:
    def __init__(self):
        print("Get the length in bytes of one array item in the internal representation")

    def len_arr(self):
        array_num = array('i', [1, 3, 5, 7, 9])
        print("Original array: " + str(array_num))
        print("Length in bytes of one array item: " + str(array_num.itemsize))

s=Array()
s.len_arr()