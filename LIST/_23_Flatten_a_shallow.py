
# flatlist = []
# for sublist in lst:
#    for item in sublist:
#       flatlist.append(item)
# print("------------------------------------------------------------")
# print ("New list is :",flatlist)
# print("-----------------------------------------------------------")
import itertools
class Check():
   def ch_flat(self):

      lst = [[19,45,44,33,30, 40], ["ram","shyam","laxman","rakesh"], [90, 33, 110, 120]]
      new_list = list(itertools.chain(*lst))
      print(new_list)

result = Check()
result.ch_flat()
