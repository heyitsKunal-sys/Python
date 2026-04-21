class Employee:
    
    language="python" # class attribute
    salary = 150000
kunal = Employee()
kunal.name = "Kunal" # instance attribute or object attribute
print(kunal.language) # accessing class attribute using object name
print(kunal.name)
print(kunal.salary)      # accessing class attribute using object name

ritika = Employee()
ritika.name = "Ritika"
print(ritika.language)  # accessing class attribute using object name
print(ritika.salary)    # accessing class attribute using object name
print(ritika.name)
kunal.language = "java" # changing class attribute value using object name
print(kunal.language) # Output: java
 # Note: Instance attributes, take preference over class attributes during assignment & 
# # retrieval. 
# here name is a attribute of object and language and salary are attributes of class as they are directly accessed by class name.
 


 #Instance vs Class attributes
# Instance attributes are specific to each object and can have different values for different objects. They are
# defined within the __init__ method of a class and are accessed using the self keyword. For example:
class Employee:
    def __init__(self, name, salary): # init is a constuructor method which is used to initialize the instance attributes of a class. It is called automatically when an object of the class is created. The self parameter is a reference to the current instance of the class and is used to access the instance attributes and methods of the class.
        self.name = name  # instance attribute
        self.salary = salary  # instance attribute
emp1 = Employee("Kunal", 150000)
emp2 = Employee("Ritika", 120000)
print(emp1.name)  # Output: Kunal
print(emp1.salary)  # Output: 150000
print(emp2.name)  # Output: Ritika
print(emp2.salary)  # Output: 120000    
# Class attributes, on the other hand, are shared among all instances of a class. They are defined directly within the class and are accessed using the class name. For example:
class Employee:
    company = "Tech Company"  # class attribute
    def __init__(self, name, salary):
        self.name = name  # instance attribute
        self.salary = salary  # instance attribute
emp1 = Employee("Kunal", 150000)
emp2 = Employee("Ritika", 120000)

print(Employee.company)  # Output: Tech Company
print(emp1.company)  # Output: Tech Company
print(emp2.company)  # Output: Tech Company




#SELF PARAMETER
class Employee:
    language = "Python"
    salary = 150000
    def getSalary(self):
       print( self.salary) # accessing class attribute using self keyword
       print(self.language) # accessing class attribute using self keyword
kunal = Employee()
kunal.language = "Java" # changing class attribute value using object name output: java because instance attribute takes preference over class attribute during assignment & retrieval
kunal.getSalary() # Output: Salary is: 150000 



#STATIC METHOD :\simply means a method that belongs to the class rather than an instance of the class. It can be called on the class itself, without needing to create an instance of the class. Static methods are defined using the @staticmethod decorator and do not have access to the instance (self) or class (cls) variables. They are typically used for utility functions that perform a specific task and do not require access to instance or class data.
# decorator is used to define a static method in a class. It is a built-in function in Python that is used to modify the behavior of a method. When a method is decorated with @staticmethod, it can be called on the class itself, without needing to create an instance of the class. Static methods do not have access to the instance (self) or class (cls) variables, and they are typically used for utility functions that perform a specific task and do not require access to instance or class data.
class Employee:
    language = "Python"
    salary = 150000
    @staticmethod
    def getSalary():
        print("Salary is: 150000") # accessing class attribute using self keyword
        print("Language is: Python") # accessing class attribute using self keyword
kunal = Employee()
kunal.language = "Java" # changing class attribute value using object name output: java because instance attribute takes preference over class attribute during assignment & retrieval
kunal.getSalary()
#output: Salary is: 150000
#         Language is: Python
# In the above code, we have defined a static method getSalary() that prints the salary and language. We can call this method using the class name or an instance of the class, and it will work without any issues.
# we dont need to write self parameter as the decorater @staticmethod indicates that the method is a static method and does not require access to instance or class variables.  