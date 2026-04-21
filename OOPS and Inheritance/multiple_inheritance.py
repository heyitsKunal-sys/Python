class Employee:
    company = "google"  
    salary = "65000000"        #base class or parent class
    def show(self):
        print ( f" the name is {self.company } and the salary is {self.salary}")

class Coder:
    language= "python"
    def printLanguages(self):
        print(f"out of all languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company : 'amazon'
    def showLanguage(self):
        print(f" the name is {self.company} and he is good with {self.language}language")

a = Employee()
a.name="kunal"
print(a.name)
b = Programmer()

b.show()
b.showLanguage()
b.printLanguages()