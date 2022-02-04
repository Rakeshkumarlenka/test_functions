# a = 10
# def my_fun():
#     #global a
#     #print("global a= ",a)
#     a = 20
#     print("Local a= ", a)
#     #globals() ['a'] += 5     # x=globals() ['a']
#     print("global a= ",globals() ['a'])
# my_fun()
# print("global a= ",a)
#
#
#
# a = 10
# def my_fun():
#     global a     #keyword
#     print("global a= ",a)
#     a = 20
#     print("modify a= ", a)
# my_fun()
# print("global a= ",a)

def another_fun1():
    x = 10
    def another_fun2():
        nonlocal x
        x += 15
        print("PRINTING IN INNER")
        print(x)
    another_fun2()
print("cALING OUTER")
another_fun1()



'''
from abc import ABC,abstractmethod
class Bird(ABC):
    @abstractmethod
    def call(self):
        pass
    @abstractmethod
    def fly_speed(self):
        pass

class Parrot(Bird):
    def call(self):
        print("chuchuuuuchuuuuuu")
    def fly_speed(self):
        print("40 km/h")

class Crow(Bird):
    def call(self):
        print("kan kaa ka ka")
    def fly_speed(self):
        print("30km/h")

p1 = Parrot()
C1 = Crow()
p1.call()
p1.fly_speed()
C1.call()
C1.fly_speed()

'''


