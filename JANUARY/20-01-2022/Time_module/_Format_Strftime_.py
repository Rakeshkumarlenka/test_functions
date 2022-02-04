#Formate the time using strftimemethod
from datetime import *
dt = datetime.now()
print(dt)

print('current time: ',dt.strftime("%H:%M:%S"))