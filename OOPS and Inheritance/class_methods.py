# A class method is a method which is bound to the class and not the object of the class. 
# @classmethod decorator is used to create a class method. 

class Employee:
    language ="python"
    a =1
    
    # def show(self):
    def show(cls):
        # print(f" the class attribute of a is {self.a}")
        print(f" the class attribute of a is {cls.a}")
                            # : the class attribute of a is 45

e = Employee()   
e.language= "javaacript"  
print(e.language)   
e.a =45   #yahan pe ye 45 dikhayega jo ki object attribute h lekin
        #   hume chahiye class attribute

e.show( )

# so we will use @classmethod and instead of self we write cls


