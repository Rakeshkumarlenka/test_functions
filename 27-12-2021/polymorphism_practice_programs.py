print("===================================================================================================")
print("===================================================================================================")
#Duck typing philosophy
#WAPP to innvoke a method an object without knowing the type (or class) of the object
class Duck:
    def talk(self):
        print('Quack, Quack !!')

class Human:
    def talk(self):
        print('Hello, Hiiiii!!!!')

def call_talk(obj):
    obj.talk()

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
print("===================================================================================================")
print("===================================================================================================")
#WAPP to check the object type to know whether the method exists in the object or not

class Dog:
    def bark(self):
        print('Boww. WOW !!!!!')

class Duck:
    def talk(self):
        print('Quack, Quack !!')

class Human:
    def talk(self):
        print('Hello, Hiiiii!!!!')

def call_talk(obj):
    if hasattr(obj, 'talk'):
        obj.talk()
    elif hasattr(obj, 'bark'):
        obj.bark()
    else:
        print("Wrong objects Passed")

x = Duck()
call_talk(x)
x = Human()
call_talk(x)
x = Dog()
call_talk(x)
print("===================================================================================================")
print("===================================================================================================")
#OPERATOR OVERLOADING
#WAPP to use addition operator to act on diffrent types of objects
#overloading the + operator
print(5+7)

#using + on strings to concanate them
s1 = 'red'
s2 = 'fort'
print(s1 + s2)

#using + on lists to make a single list
a = [2,3,4,5,6]
b = [9,7,8,4,0]
print(a+b)
print("===================================================================================================")
print("===================================================================================================")
#WAPP to overload  the + operator to make it act on class objects
class BookX:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self,other):
        return self.pages+other.pages
class BookY:
    def __init__(self,pages):
        self.pages = pages

b1 = BookX(100)
b2 = BookY(200)
print('Total pages =',b1+b2)
print("===================================================================================================")
print("===================================================================================================")
#Overloading > operator
class Ramayan:
    def __init__(self,pages):
        self.pages = pages

    def __gt__(self,other):
        return self.pages>other.pages

class Mahabhart:
    def __init__(self,pages):
        self.pages = pages

b1 = Ramayan(1000)
b2 = Mahabhart(1700)
if (b1>b2):
    print('Ramayan has more pages')
else:
    print('mahabharat has more pages')
print("===================================================================================================")
print("===================================================================================================")