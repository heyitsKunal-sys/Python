#  property decorator
# Consider the following class:  
class Employee: 
    @property
    def name(self):
        return f"{self.fname } {self.lname }"
    @name.setter 
    def name (self,value): 
        self.fname = value.split(" ")   [0]
        self.lname = value.split(" ")   [1]
e = Employee()        
e.name = "kunal bhardwaj"
print(e.name)                   #output:kunal bhardwaj kyuki name se koi attribute humne nahi bnaya tha class me

# If e = Employee() is an object of class employee, we can print (e.name) to print the 
# ename by internally calling name() function. 

# property decorator me hume pure function ko call krne ki nee nahi hoti h . ye hume kuch bhi return krva deta hai
class Student:
    def get_name(self):
        return "Kunal"

s = Student()
print(s.get_name())   # method call  

# But with @property, you can do:

class Student:
    @property
    def name(self):
        return "Kunal"

s = Student()
print(s.name)   # looks like variable (no brackets)


class Employee:
    def __init__(self, salary):
        self.salary = salary

    @property
    def bonus(self):
        return self.salary * 0.10

e = Employee(10000)
print(e.bonus)  # sidha value return karega
# print(e.bonus()) agar property use nahi kiyahota to...