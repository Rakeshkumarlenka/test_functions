#swap comma and dot in a string

class Swapc_d():
    def sw_replace(self,str1):
        maketrans = str1.maketrans
        final = str1.translate(maketrans(',.', '.,', ' '))
        return final.replace(',', ", ")


string = "14, 625, 498.002"
swapp = Swapc_d()
print(swapp.sw_replace(string))