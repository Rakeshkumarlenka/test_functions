#Reverse a given string  Input : "Python"   Output : "nohtyP"

class String_probs():
    def reverstr(self):
        in_str = input("Please enter a String: ")
        s = ""
        for ch in in_str:
            s = ch + s
        print("The reversed string is: ", s)

res = String_probs()
res.reverstr()