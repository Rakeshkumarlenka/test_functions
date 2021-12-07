class Str_Vowels:
    def __init__(self,str):
        self.str = str
    def result(self):
        Vowels = 'aeiuoAEIUO'
        final = []
        for word in str:
            if word in Vowels:
                final.append(word)
        print("-" * 50)
        print("Find the vowels from a string:",final)
        print("-" * 50)
        print("Count and display the vowels of the given string:",len(final))
        print("-" * 50)
print("-" * 50)
str = input("enter your string:")
print("-" * 50)
s = Str_Vowels(str)
s.result()