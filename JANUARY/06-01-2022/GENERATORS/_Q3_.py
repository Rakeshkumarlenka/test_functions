print("List Iteration")
l = [3,5,6,'ram','shyam']
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ('hi','welcome','to','python')
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "welcome to the world"
for i in s:
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))