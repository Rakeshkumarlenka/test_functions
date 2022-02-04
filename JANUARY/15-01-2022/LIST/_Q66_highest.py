#Find the list in a list of lists whose sum of elements is the highest
class List_probs:
    def element_high(self):
        num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
        print(max(num, key=sum))

res = List_probs()
res.element_high()