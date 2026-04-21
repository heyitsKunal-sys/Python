#  super() method is used to access the methods of a super class in the derived class. 
#  super().__init__() 
# __init__() Calls constructor of the base class 
class Employee:
    def __init__(self):
        print("constructor of Employee")
    a= 1
    d =2

class Programmer(Employee):
    def __init__(self):
        print("constructor of Programmer")
    b =1
    f=3

class Manager(Programmer):
    def __init__(self):
        super().__init__()   #is func se programmer or manager dono ka print hoga
        print("constructor of Manager")
    c =3   


o = Employee()    
print(o.a )       #print attribute
# print(o.b)        # error: Employee' object has no attribute 'b'
o1 = Programmer()
print(o1.d)       #print: 2
o2 =Manager()
print(o2.f)       #print: 3