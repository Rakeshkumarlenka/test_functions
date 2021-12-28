class Remove:
    def rem_spac(self):
        Product_list = {'P 01': 'DBMS', 'P 02': 'OS',
                        'P 0 3 ': 'Soft Computing'}
        Product_list = {x.translate({32: None}): y
                        for x, y in Product_list.items()}
        print(" New dictionary : ", Product_list)

res = Remove()
res.rem_spac()