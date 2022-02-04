class Str_probs():
    def solve(self):
        s = "programming"
        s = list(s)
        for i in range(0, len(s) - 1, 2):
            s[i], s[i + 1] = s[i + 1], s[i]
        print( ''.join(s))


res = Str_probs()
res.solve()