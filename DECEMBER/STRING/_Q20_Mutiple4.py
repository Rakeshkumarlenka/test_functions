class Str_prob():
    def reverse_string(self):
        name = input("enter a name:")
        if (len(name) % 4 == 0):
            print(name[::-1])
        else:
            print("cant")


res = Str_prob()
res.reverse_string()