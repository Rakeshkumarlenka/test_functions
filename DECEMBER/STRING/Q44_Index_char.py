class Index():
    def in_char(self):
        res = None
        for i in range(0, len(in_str)):
            if in_str[i] == c:
                res = i + 1
                break

        if res == None:
            print("No such character available in string")
        else:
            print("Character {} is present at {}".format(c, str(res)))

in_str = 'abcdrakesh'
c = input("enter the character which you want to know the index:")
result = Index()
result.in_char()