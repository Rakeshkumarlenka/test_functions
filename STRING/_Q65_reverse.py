class Str_prob():
    def reverse(self):
        s = input("Enter the string: ")
        w = s.split(" ")
        nw = [i[::-1] for i in w]
        ns = " ".join(nw)
        print( ns)


res = Str_prob()
res.reverse()


