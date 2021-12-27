'''Write 3D arrray'''
class Array:
    def __init__(self,rows,col):
        self.rows=rows
        self.col=col
    def creating_array(self):
        mylist=[[0 for c in range(col) ]for r in range(rows)]
        for r in range(rows):
            for c in range(col):
                mylist[r][c]=r*c
                print(mylist)

col=int(input("enter the number of coloums"))
rows=int(input("enter the number of rows"))
a=Array(rows,col)
print(a.creating_array())