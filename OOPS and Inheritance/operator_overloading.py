# Operators in Python can be overloaded using dunder methods. 
# These methods are called when a given operator is used on the objects. 
class Number:
    def __init__(self ,n):
        self.n = n
    
    def __add__(self , num):
        return self.n + num.n   
    def __sub__(self , num):
        return self.n - num.n       
          
 

    
n = Number(1)
m = Number(2)

print(n +m)                    #output: 3 
print(n - m)                   # -1


# Other dunder/magic methods in Python: 
# str__() # used to set what gets displayed upon calling str(obj) 

# __len__() # used to set what gets displayed upon calling.__len__() or 
# len(obj)

class Employee:
    name = "google"
    def __str__(self ):
        return self.name

    def __len__(self):
        return len(self.name)   


obj = Employee()
 print(obj)                      #google
           
                            
 print(len(obj))                  # 6
      
    
         
          