#ipaddress
def check_ip(ip):
    masklist = ip.split("/")
    mask = masklist[-1]
    masklist = masklist[0:(len(masklist)-1)]
    ip = ".".join(masklist)
    new_ip = ".".join([str(int(i)) for i in ip.split(".")]) 
    new_ip = new_ip +"/"+ mask

    return new_ip
 
ip ="00000000192.000000166.0000000/24"
print(check_ip(ip))