
#calculate the sum
a = lambda x, y:x+y
res = a(34, 32)
print('sum is :',res)

x = lambda a, b, c: a + b + c
print(x(5, 4, 2))


#lambda function use for calculate the square of a number
in_lam = lambda x : x*x
value = in_lam(5)
print('square is ',value)

#Find Biggest no
max = lambda x,y: x if x > y else y
a ,b = [int(n) for n in input('Enter two no:').split(',')]
print('bigger no :', max(a,b))

#
def myfunc(n):
  return lambda a : a * n

res = myfunc(2)
print(res(10))