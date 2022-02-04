# Print a nested lists (each list on a new line) using the print() function
class List_probs:
        def nes_list(self):
                nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]]
                for ns_lst in nested_list:
                        print(' '.join(str(x) for x in ns_lst))

res = List_probs()
res.nes_list()

