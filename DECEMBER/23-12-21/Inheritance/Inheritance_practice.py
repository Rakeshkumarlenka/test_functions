print('=============================INHERIATNCE========================')
class Father:
    def __init__(self):
        self.property = 800000.00

    def display_prop(self):
        print('father\'s property =',self.property)

class Son(Father):
    pass

s = Son()
s.display_prop()
print('==================================================================================')
'''overriding the base class constructor and method in sub class'''
class Father_in:
    def __init__(self):
        self.property = 800000.00

    def display_prop(self):
        print('father\'s property =',self.property)

class Son_in(Father_in):
    def __init__(self):
        self.property = 200000.00

    def display_prop(self):
        print('Child\'s property =',self.property)


s = Son_in()
s.display_prop()
print('==================================================================================')
print('==================================================================================')


