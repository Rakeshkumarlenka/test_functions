#create intersection of sets

#remove the element if element is available

class Demo:
    def __init__(self):
        pass
    def create(self):
        a=set()
        b=set()
        print("first set")
        a1=int(input("how many values"))
        for i in range(a1):
            a2=int(input("enter the elementss"))
            a.add(a2)
        print("second set")
        b1 = int(input("how many values"))
        for i in range(a1):
            b2=int(input("enter the elementss"))
            b.add(b2)

        print(a.intersection(b))

d=Demo()
d.create()