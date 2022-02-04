# def prob(x,y):
#     while x<=y:
#         yield x
#         x+=1
# g = prob(3,10)
# for i in g:
#     print(i)


my_list = [4, 7, 0, 3]
print(my_list)         # my_list.__str__()
for each in my_list:
    print(each)

my_list = [4, 7, 0, 3]
my_iter = my_list.__iter__()

print("ITERATOR object : ", my_iter)
print("Consecutive elements")
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())