# print the following floating numbers with no decimal places
class Str_pro:
    def str_dec(self):
        x = float(input("Enter First Number: "))
        y = float(input("Enter Second Number: "))
        print("Original Number:", x , "and" ,y)
        print("Floating number with no decimal places:" + "{:.0f}".format(x))
        print("Floating number with no decimal places:" + "{:.0f}".format(y))

res = Str_pro()
res.str_dec()



