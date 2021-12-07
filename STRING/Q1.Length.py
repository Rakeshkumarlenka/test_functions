class Lenstr():
    def findLen(self):
        counter = 0
        for i in str:
            counter += 1
        return counter

str = "welcome to python"
new_len = Lenstr()
print("-"*30)
print("Length of the string is:",new_len.findLen())
print("-"*30)