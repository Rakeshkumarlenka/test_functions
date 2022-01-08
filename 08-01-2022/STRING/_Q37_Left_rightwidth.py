#to display a number in left, right and center aligned of width 10
class Str_pro:
    def str_aligned(self):
        x = int(input("Enter your Number:"))
        print("Original Number:", x)
        print("Left aligned (width 10):" + "{:< 10d}".format(x))
        print("Right aligned (width 10):" + "{:10d}".format(x))
        print("Center aligned (width 10):" + "{:^10d}".format(x))

res = Str_pro()
res.str_aligned()
