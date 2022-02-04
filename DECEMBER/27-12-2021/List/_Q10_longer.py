'''words longer then the element'''
class String:
    def __init__(self,str1,k):
        self.str1=str1
        self.k=k

    def words_len(self):
        string=[]
        str1=str.split(" ")
        for i in str1:
            if len(i)>k:
                string.append(i)
                return string


str1="Hi welcome"
k=5
length=String(str1,k)
result=length.words_len()
print("words longer then the element",result)