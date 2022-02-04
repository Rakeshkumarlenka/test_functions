#overriding
class Car:
    def sound(self):
        print("VROOOOM")

class Bugatti(Car):
    def sound(self):
        print("VVVVRRRROOOMMM")

b = Bugatti()
b.sound()


#overloading
def add(kind, *args):
    if kind == "int":
        sum = 0

    if kind == "string":
        sum = ""

    for i in args:
        sum = sum + i

    return sum

print(add("int",10,20,30))
print(add("string","hello"," welcome"))
