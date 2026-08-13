class Employee:
    pass
e = Employee()
e.name = "kunal"
print(e.name)   ##prints :kunal
#python does like store "kunal" inside e's name.
#but i want to seperate it into fname and enam.
#"kunal bhardwaj"..
#fname ="kunal" lname ="bhardwaj"
# now if we simply do e.name = "kunal bhardwaj" python stores it not seperates it
# basically setter is a gatekeeper 
# you give kunal bhardwaj
# setter seperates the name 
# so when we write e.name = "kunal bhardwaj"
# setter recieves it as: value ="kunal bhardwaj"
# then value is split(" ") gives ["kunal", "bhardwaj"]
# so f.name = "kunal"
# l.name ="bhardawaj"

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
print(e.name) 

# what does property do??
# think property as a another gatekeeper:
# so: print(e.name) doesnot simply retrieve a stored name
# e.name -> @property -> "kunal"+"bhardwaj" ->"kunal bhardwaj"
# when u write e.name = "kunal bhardwaj" because of setter python stores
# e -> fname= "kunal" lname:"bhardwaj"
# then when you write print(e.name) @property funtion runs: "fname" + "ename"