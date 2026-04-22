# Q1. Create a class (2-D vector) and use it to create another class representing a 3-D vector
class TwoDvector:
    def __init__(self , i ,j):
        self.i = i
        self.j = j

    def show(self):
            print(f"the vector is {self.i}i + {self.j}j ")


class ThreeDvector(TwoDvector):
    def __init__(self,i,j,k):
        super().__init__(i ,j )

        self.k =k

    def show(self):
            print(f"the vector is {self.i}i + {self.j}j + {self.k}k")     



a =TwoDvector(1,2)
a.show()
b= ThreeDvector(1,2,3)
b.show()
# output: the vector is 1i + 2j 
# the vector is 1i + 2j + 3k
        

# Q2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.         
         
class Animals:
    
    pass

class Pets(Animals):
    
    pass

class Dog(Pets):
    @staticmethod
    def bark():
        print("bow bow")

d = Dog()
d.bark()        

# Q3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary. 

# You have an Employee with:

# salary (base salary)
# increment (percentage increase)

# You need:

# A derived value → salaryAfterIncrement
# This is not stored directly.
# It’s calculated from salary and increment.
# A setter for salaryAfterIncrement
# If someone sets a new final salary, you should recalculate the increment automatically.

# 👉 So:

# Getter → computes final salary
# Setter → updates increment based on desired final salary

class Employee:
    salary = 234
    increment = 20
    @property  
    def salaryAfterIncrement(self):
        return (self.salary + self.salary *self.increment /100)
    
    @salaryAfterIncrement.setter                                                         #final salary=salary+(salary×100increment​)
                                                                                        
    def salaryAfterIncrement(self,salary):
        self.increment =((salary/self.salary - 1) *100)
        #increment=(old salarynew salary​−1)×100
          
        return 



e = Employee()
print(e.salaryAfterIncrement) #280.8

print(e.increment)

#  Q4"Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imag = self.r * c2.i + self.i * c2.r
        return Complex(real, imag)

    def __str__(self):
        return f"{self.r} + {self.i}i"

#here self means c1
c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)   # 4 + 6i
print(c1 * c2)   # -5 + 10i