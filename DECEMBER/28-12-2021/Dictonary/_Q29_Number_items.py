#Count number of items in a dictionary value that is a list
class Number:
    def no_items(self):
        dict = {'Arana': ['subj1', 'subj2', 'subj3'], 'Dhurv': ['subj1', 'subj2']}
        ctr = sum(map(len, dict.values()))
        print(ctr)

res = Number()
res.no_items()