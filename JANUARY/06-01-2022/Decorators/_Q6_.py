def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)
print(add_15(10))
add_5 = create_adder(5)
print(add_5(10))
add_15 = create_adder(15)
print(add_15(34))
add_1 = create_adder(1)
print(add_1(14))




