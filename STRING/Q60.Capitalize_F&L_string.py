
class Captf_l():
    def convert(self, str1):
        str1 = result = str1.title()
        result = ""
        for word in str1.split():
            result += word[:-1] + word[-1].upper() + " "
        return result[:-1]


sent = "python exercises practice solution"
cap_conv = Captf_l()
print("new string is :\n", cap_conv.convert())
