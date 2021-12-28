#Sort Counter by value.
class Sort:
    def sort_counter(self):
        from collections import Counter
        x = Counter({'Math': 81, 'Physics': 83, 'Chemistry': 87})
        print(x.most_common())

res = Sort()
res.sort_counter()