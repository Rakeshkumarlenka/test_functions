class Last_str:
    def __init__(self,str):
        self.str = str
    def last_part(self):
        for word in str.split():
            if word == word[-1]:
                pass
        print(word)

str = input("Enter full string:")
l = Last_str(str)
l.last_part()