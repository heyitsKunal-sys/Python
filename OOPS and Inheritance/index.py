# inheritance means creating a new class from existing class

class Employee:
    company = "google"          #base class or parent class
    def show(self):
        print ( f" the name is {self.name } and the salary is {self.salary}")

# class Programmer :
#     company = "amazon"
#     def show(self):
#         print(f" the name is {self.name} and salary is {self.salary}")
    
#     def showLanguage(self):
#         print(f" the name is {self.name} and he is good with {self.language}language")


class Programmer(Employee):
    company = "amazon"
    def show(self):
        print(f" the name is {self.name} and he is good with {self.language}language")

                                #  inherited class
a = Employee()
b = Programmer()
print(a.company , b.company )       

    
    