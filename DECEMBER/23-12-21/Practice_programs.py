print('=======================STATIC METHOD===============================')

#Static method
class Staticlass():
    @staticmethod
    def my_method(x,n):
        result = x ** n
        print('{} to the power of {} is {}'.format(x,n,result))

res = Staticlass()
res.my_method(5,3)
res.my_method(8,4)
print('==================================================================================')
class Myclass:
    n=0
    def __init__(self):
        Myclass.n = Myclass.n+1

    @staticmethod
    def no_objects():
        print('No of instances created :',Myclass.n)

obj1 = Myclass()
obj2 = Myclass()
obj3 = Myclass()
obj4 = Myclass()
Myclass.no_objects()



print('==================================================================================')
class Employee:
    def __init__(self,id,name,salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print('id=',self.id)
        print('name=', self.name)
        print('salary=', self.salary)

class My_static:
    @staticmethod
    def mymethod(e):
        e.salary+=1000;
        e.display()

e = Employee(122,'Rakesh',16000.65)
My_static.mymethod(e)

print('==================================================================================')
'''Static method is using when we want to pass some values from outside and perform some calculations'''

print('==================================================================================')
'''static method to find Square root value'''
import math
class Sample:
    @staticmethod
    def calculate(x):
        result = math.sqrt(x)
        return result
num = float(input('Enter a no:'))
res = Sample.calculate(num)
print('The square root of {} is {:.2f}'.format(num,res))

print('==================================================================================')
print('====================INNER CLASS=================================')
class Person:
    def __init__(self):
        self.name = 'Rakesh'
        self.db = self.Dob()

    def display(self):
        print("Name=",self.name)

    class Dob():
        def __init__(self):
            self.dd = 25
            self.mm = 5
            self.yy = 1995
        def display(self):
            print('DOB= {}/{}/{}'.format(self.dd,self.mm,self.yy))

p = Person()
p.display()

x= p.db
x.display()

print('==================================================================================')
