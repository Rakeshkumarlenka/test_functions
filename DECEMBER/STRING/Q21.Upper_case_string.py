#
class Upper_case():
    def con_up(self):
        string1 = ''
        for i in range(len(in_str)):
            if (in_str[i] >= 'a' and in_str[i] <= 'z'):
                string1 = string1 + chr((ord(in_str[i]) - 32))
            else:
                string1 = string1 + in_str[i]
        print("-"*40)
        print ("New converted string is :\n",string1)
        print("-" * 40)


up = Upper_case()
in_str = input("Please Enter your Own String : ")
up.con_up()
