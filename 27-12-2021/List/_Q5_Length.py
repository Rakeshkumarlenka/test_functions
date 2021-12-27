'''count number of strings whose length is 2'''
class Number:
    def __init__(self,str1):
        self.str1=str1

    def count_num(self):
        for ele in str1:
            if len(ele)==2:
                return ele
str1=["add","ll","aff","yuir","poio","kk","yy"]
string_len=Number(str1)
result=string_len.count_num()
print("count number of strings whose length is 2 :",result)