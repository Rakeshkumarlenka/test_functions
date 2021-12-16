m = {6, 4, 2, 7, 9}
print("The original set is : " + str(set(m)))
K = 7
res = -1
for ele in m:
    res += 1
    if ele == K:
        break

print("Position of K in set : " + str(res))


n = {6, 4, 2, 7, 9}
f = {5,6,7,8}
k = n.update(f)
print(n)
