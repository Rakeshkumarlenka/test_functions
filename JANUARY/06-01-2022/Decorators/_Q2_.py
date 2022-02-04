#decorator to to increase the value of a function by 2 by @decor
def decor(fun):
    def innner():
        value = fun()
        return value + 2
    return innner

@decor
def num():
    return 23

print(num())