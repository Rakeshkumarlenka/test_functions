import random as r

x = random.seed(24)

b = random.random()
print(b)

c = random.randint(1,100)


a = ['hi','helo','welcome','hehhe','hgffs','ghjgs']
print(r.choices(a,k = 2,weights=[1,2,4,5,77,222]))


