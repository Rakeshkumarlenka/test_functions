#Check multiple keys exists in a dictionary.

class Check_mul:
    def multi_keys(self):
        student = {'name': 'Arunn','address':'Bangalore','emp_id': '5002'}
        print(student.keys() >= {'address', 'name'})
        print(student.keys() >= {'name', 'Arunn'})
        print(student.keys() >= {'emp_id', 'name'})

res = Check_mul()
res.multi_keys()

