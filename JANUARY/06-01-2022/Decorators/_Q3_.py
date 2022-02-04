def decor(fun):
    def inner():
        value = fun()
        return value+3
    return inner

def decor1(fun):
    def inner():
        value = fun()
        return value * 3
    return inner

@decor
@decor1
def num():
    return 20
print(num())