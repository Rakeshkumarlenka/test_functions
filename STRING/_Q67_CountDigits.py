#that accepts a string and calculate the number of digits and letters

class String_probs():
    def cou_digi_num(self):
        s = input("Input a string")
        d = l = 0
        for c in s:
            if c.isdigit():
                d = d + 1
            elif c.isalpha():
                l = l + 1
            else:
                pass
        print("Letters", l)
        print("Digits", d)

res = String_probs()
res.cou_digi_num()