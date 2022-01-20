#P1: Time in seconds

import time
epoch = time.time()
print(epoch)


#P2: Converting epoch time in to date and time

t = time.localtime(1642669019.2189999)

d = t.tm_mday
m = t.tm_mon
y = t.tm_year
print('Current date is : %d - %d - %d ' %(d,m,y))

h = t.tm_hour
m = t.tm_min
s = t.tm_sec
print('Current time is : %d : %d : %d ' %(h,m,s))


#P3: Converting epoch time in to date and time

t = time.ctime(1642669019.2189999)
print(t)

#P4: Current date and time using ctime()
t = time.ctime()
print(t)