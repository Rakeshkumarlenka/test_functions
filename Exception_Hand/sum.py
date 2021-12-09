try:
    class Sum():
        def check(self):
            m=a+b
            print (m)

    a=int(input("enter the no:"))
    b=int(input("enter the no:"))
    result =Sum()
    result.check()
except ValueError as va:
    print("error an occure",va)
finally:
    print("it is excuted")