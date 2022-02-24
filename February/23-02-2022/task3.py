lst = [1,2,3,1,2,3,1,2,3,4,3,2,1]

'''
Output:=
[1,1,1,1] = 1
[2,2,2,2] = 16
[3,3,3,3] = 81
[4] = 4
sum = 102
'''
outlist = []
sum_list=[]
sum = 0
while(lst):
    num = lst[0]
    count_num = lst.count(num)
    n= pow(num,count_num)
    sum_list.append(n)
    print(sum_list)
    sum+=n
    while(num in lst):
        try:
            lst.remove(num)
        except:
            pass 
    
print("total sum is:-", sum)