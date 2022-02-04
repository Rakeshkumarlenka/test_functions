# #instance variable & instance method
# class Student:
#     def __init__(self): #constructor
#         self.name = 'vicky'
#         self.age = 27
#         self.marks = 877
#
#     def view(self): #instance method
#         print('Hi i am',self.name)
#         print('my age is',self.age)
#         print('marks obtained is ',self.marks)
#
# res = Student() #instance of student class
# res.view() #caling method with instance



class Student1:
    def __init__(self,n ='',m=0):
        self.name = n
        self.age = m

    def view(self):
        print('Hi i am',self.name)
        print('my age is',self.age)

#constructor without arguments
res = Student1()
res.view()

#constructor with called 2 arguments
res1 = Student1('Reshma',600)
res1.view()

'''
class New_pro:
    def __init__(self):
        self.x = 10

    @classmethod #decorator
    def modify(cls): #cls is the default parameter of classmethod
        cls.x +=1  #cls.x is the class variable

#2 instances
res2 = New_pro()
result = New_pro()
print ('x in res2=',res2.x)
print ('x in result=',result.x)

res2.modify()
print ('x in res2=',res2.x)
print ('x in result=',result.x)
'''

class Bird:
    wings = 2
    @classmethod
    def fly(cls,name):
        print("{} flies with {} wings".format(name,cls.wings))

Bird.fly("piegon")
Bird.fly("sparrow")






