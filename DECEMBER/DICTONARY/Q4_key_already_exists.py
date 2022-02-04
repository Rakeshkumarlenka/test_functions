class Ch_key:
    def check(self,dict,key):
        self.dict = dict
        self.key = key
        if key in dict:
            print("-" * 40)
            print("Key is present")
            print("-" * 40)
            print("value is =",dict[key])
            print("-" * 40)
        else:
            print("not present")
dict = {'a': 100, 'b':200, 'c':300, 'hii':'welcome', 'news':'rain'}
print("-"*40)
key = input("enter your key which you want to check:")
result = Ch_key()
result.check(dict,key)