class Dicttable:
    def dict_print_table(self,dict1):
        print('Name', '\t', 'jersey number')
        for (x1, x2) in zip(dict1.keys(), dict1.values()):
            print(x1, '\t', x2)

print("------------------------------------------")
dict1={'sachin':10,'virat':18,'dhoni':7}
a1=Dicttable()
a1.dict_print_table(dict1)
print("------------------------------------------")
