#print the following integers with '*' on the right of specified width
class Width:
    def spec_wid(self):
        x = int(input("Enter your Number:"))
        print("Original Number:", x)
        print("Integers with zeros on the right of specified width :" + "{:*<3d}".format(x))

res = Width()
res.spec_wid()


