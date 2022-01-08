#Replace the last element in a list with another list

class List_probs:
    def replaceis(self):
        num1 = [1, 3, 5, 7, 9, 10]
        num2 = [2, 4, 6, 8]
        num1[-1:] = num2
        print(num1)

res = List_probs()
res.replaceis()

