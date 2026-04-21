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