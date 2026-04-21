class Employee:
    a= 1
    d =2

class Programmer(Employee):
    b =1
    f=3

class Manager(Programmer):
    c =3   


o = Employee()    
print(o.a )       #print attribute
# print(o.b)        # error: Employee' object has no attribute 'b'
o1 = Programmer()
print(o1.d)       #print: 2
o2 =Manager()
print(o2.f)       #print: 3