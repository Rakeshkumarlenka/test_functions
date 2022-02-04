class Dict_line:
    def dict_rep(self):
        students = {'Arun': {'class': 'V',
                            'rolld_id': 12},
                    'Pooja': {'class': 'V',
                             'roll_id': 33}}
        for a in students:
            print(a)
            for b in students[a]:
                print(b, ':', students[a][b])

res = Dict_line()
res.dict_rep()