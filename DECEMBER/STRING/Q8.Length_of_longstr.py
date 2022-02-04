#Length of longest string in python

class Len_Longest_Str:
    def __init__(self,len_str):
        self.len_str = len_str
    def result(self):
        max_len = 0
        for ele in len_str:
            if len(ele)>max_len:
                max_len = len(ele)
                res = ele
        print("-"*30)
        print("Longest string in list:\n",res)
        print("-" * 30)
        print("length of longest string in list:",len(res))
        print("-" * 30)

len_str = ['ram is a good boy','its rainning','hello','good','ram']
l = Len_Longest_Str(len_str)
l.result()