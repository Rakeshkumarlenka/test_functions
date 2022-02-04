class Count:
    def __init__(self,in_str,char):
        self.in_str = in_str
        self.char = char
    def count_str(self):
        for ele in in_str.split():
            if ele == char:
                pass
        print(in_str.count(char))
in_str = input("Enter your string:")
char = input("Enter your character:")
c = Count(in_str,char)
c.count_str()


