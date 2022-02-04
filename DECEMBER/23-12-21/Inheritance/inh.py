from teacher import Teacher
t = Teacher()
t.setid(10)
t.setname('rakesh')
t.setaddress('hn-52,hopefarm,Blr')
t.setsalary(25000.50)

print('id=', t.getid(id))
print('name=', t.getname('name'))
print('address=', t.getaddress('address'))
print('salary=', t.getsalary('salary'))

