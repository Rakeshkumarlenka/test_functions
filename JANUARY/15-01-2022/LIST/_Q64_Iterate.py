#Iterate over two lists simultaneously
class List_probs:
    def iterate(self):
        num = [1, 2, 3]
        color = ['red', 'white', 'black']
        for (a, b) in zip(num, color):
            print(a, b)

res = List_probs()
res.iterate()