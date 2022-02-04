#Reverse each word and reverse word again. Input

class String_probs():
    def reverstr(self):
        in_str = input("Please enter a String: ")
        s = ""
        m = ""
        for ch in in_str:
            s = ch + s
        print("The reversed string is: ", s)
        for ch in s:
            m = ch + m
        print("The new string is: ", m)

res = String_probs()
res.reverstr()