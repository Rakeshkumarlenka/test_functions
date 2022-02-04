class Str_probs():
    def first_three(self):
        in_str = input("Enter the string:")
        print( in_str[:3] if len(in_str) > 3 else in_str)

res = Str_probs()
res.first_three()

