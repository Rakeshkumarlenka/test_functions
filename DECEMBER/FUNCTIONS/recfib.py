def recfib(n):
    if(n<=1):
        return n
    else:
        return recfib(n-1)+recfib(n-2)

n = int(input("Enter no of terms : "))
for i in range(n):
    print(recfib(i))