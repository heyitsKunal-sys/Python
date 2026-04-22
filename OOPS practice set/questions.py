# Create a class “Programmer” for storing information of few programmers 
#   working at Microsoft. 

class Programmer :
    company ="microsoft"

    def __init__(self, name, salary):
        
        self.name = name
        self.salary= salary

Employee1 = Programmer("kunal" , 15000000 )
print(Employee1.name)
print(Employee1.salary)
Employee2 = Programmer("ritika" , 15000000 )
print(Employee2.name)
print(Employee2.salary)
print(Employee2.company)


#  Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")



a = Calculator(4)        
a.square( )
a.cube()
a.squareroot()


# Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’. Does this change the class attribute? 
class Demo:
    a = 4

o = Demo()
print(o.a)     #prints 4 class attribute beacuse there is no instance attribute present
o.a =0         #we provide instance attribute
print(o.a)     #here instance attribute 0 gets print 
print(Demo.a)  #but if we print demo.a then it prints 4

#Add a static method in problem 2, to greet the user with hello. 
class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")
    @staticmethod    
    def hello():
        print("hello world  ")    



a = Calculator(4)        
a.square( )
a.cube()
a.squareroot()
a.hello()

#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi") 
# fro and to are just parameters (variables)
# They represent:

# fro → starting place (source)
# to → destination place           we cannot use from beacuse it is resreve keyword in python

# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects??????

from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} is running on time")

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint(222,555)}")

t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi") 