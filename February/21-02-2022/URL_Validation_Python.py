
import requests

r = requests.get('https://httpbin.org/',)

print(r)  #<Response [200]>


r = requests.get('https://httpbin.org/basic-auth/rakesh/request', auth=('rakesh', 'request'))

print(r)
print(r.text)



