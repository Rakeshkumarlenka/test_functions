class Convert:
    def con_nes(self):
        num_list = [1, 2, 3, 4]
        new_dict = current = {}
        for name in num_list:
            current[name] = {}
            current = current[name]
        print(new_dict)

res = Convert()
res.con_nes()