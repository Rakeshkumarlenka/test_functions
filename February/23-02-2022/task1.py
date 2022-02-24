def reverseword(str1): 
   w = str1.split(" ")        
   nw = [i[::-1] for i in w]                        
   ns = " ".join(nw)
   return ns

str1 = "welcome to python"
print(reverseword(str1))