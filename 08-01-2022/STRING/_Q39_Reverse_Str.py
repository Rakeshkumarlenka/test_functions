#reverse a string
class Str_pro:
    def str_rev(self):
        txt = input("enter your String:")
        res = ""
        for char in txt:
            res = char + res
        print(res)

res = Str_pro()
res.str_rev()
