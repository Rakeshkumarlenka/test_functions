
class Remo_new():
    def new_line(self):
        res = []
        for sub in test_list:
            res.append(sub.replace("\n", ""))
        print(str(res))

test_list = ['hell\no', 'h\ni', 'py\nthon', 'i\ns', 'goo\nd', 't\no' ,'learn\n']
result = Remo_new()
result.new_line()




