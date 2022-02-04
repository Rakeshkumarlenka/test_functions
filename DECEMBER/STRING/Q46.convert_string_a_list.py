class Cons_l():
    def Convert(self,string):
        li = list(string.split(" "))
        return li

str1 = "welcome to python world"
conver = Cons_l()
print(conver.Convert(str1))