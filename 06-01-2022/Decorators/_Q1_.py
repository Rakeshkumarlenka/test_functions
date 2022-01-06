print('--------------------------------------------------')
print('--------------------------------------------------')
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

resu = operate(inc,3)
resu2 = operate(dec,3)
print(resu)
print(resu2)


print('--------------------------------------------------')
print('--------------------------------------------------')
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")

rese = make_pretty(ordinary)
print(rese())






print('--------------------------------------------------')
print('--------------------------------------------------')
#decorator to to increase the value of a function by 2
def decor(fun):
    def innner():
        value = fun()
        return value + 2
    return innner

def num():
    return 23
res = decor(num)
print(res())
print('--------------------------------------------------')
print('--------------------------------------------------')