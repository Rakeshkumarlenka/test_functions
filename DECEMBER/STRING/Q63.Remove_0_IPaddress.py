#remove leading zeros from an IP address
class Remove():
    def rem_ip(self,ip):
        zeroip = ".".join([str(int(i)) for i in ip.split(".")])
        return zeroip;


Ip = Remove()
print("-"*40)
ip = input("Enter the IP address :  \n")   #200.006.020.900
print("-"*40)
print("New Ip Address : ", Ip.rem_ip(ip))   #200.6.20.900
print("-"*40)
