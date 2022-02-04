#WAPP Single Inheritance in which two sub classes are derived a single base class
#Single Inheritance
class Bank(object):
    cash = 100000000
    @classmethod

    def available_cash(cls):
        print(cls.cash)

class Andhrabank(Bank):
    pass

class StateBank(Bank):
    cash = 200000000
    @classmethod
    def avialable_cash(cls):
        print(cls.cash + Bank.cash)

a = Andhrabank()
a.available_cash()

s = StateBank()
s.available_cash()

print("===================================================================================================")
print("===================================================================================================")

#mutiple Inheritance
#WAPP to impliment mutiple inheritance using two base class
class Father:
    def height(self):
        print("height is 5.9 foot")

class Mother:
    def color(self):
        print('Color is brown')

class Child(Father,Mother):
    pass

c = Child()
print('child\'s inherited qualities:')
c.height()
c.color()
print("===================================================================================================")
print("===================================================================================================")
#WAPP to prove that only one class constructor is available to sub class in multiple inheritance
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)

class B(object):
    def __init__(self):
        self.b ='b'
        print(self.b)

class C(A , B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()

o = C()

print("===================================================================================================")
print("===================================================================================================")
#WAPP to access all the instance variable of both the base classes in mutiple inheritance
class A(object):
    def __init__(self):
        self.a = 'a'
        print(self.a)
        super().__init__()

class B(object):
    def __init__(self):
        self.b = 'b'
        print(self.b)
        super().__init__()

class C(A,B):
    def __init__(self):
        self.c = 'c'
        print(self.c)
        super().__init__()

o = C()
print("===================================================================================================")
print("===================================================================================================")

