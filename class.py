class Demo:
    # Static variable (class variable)
    """example class for types of variables"""
    static_var = "I am static!"
 
    def __init__(self, value):
        # Instance variable
        self.instance_var = value
        
        
    def printage(self):
        print(self.age)

    def show(self):
        # Local variable
        local_var = "I am local!"
        print("Instance variable:", self.instance_var)
        print("Static variable:", Demo.static_var)
        print("Local variable:", local_var)
print(Demo.static_var) # I am static!
obj = Demo("Kiran")
obj1 = Demo("Vijaya")
obj.static_var = "I am Kiran "
print(obj.static_var)
print(obj1.static_var)
print(Demo.static_var)
obj.show()

#Use instance variables → when data is different for each object
#Use static variables → when data is common to all objects
Demo.static_var="We the People of USA"
print(Demo.static_var)
print(obj1.static_var)

# Instance variables overrides class variables
class overr:
    x=10

    def __init__(self):
        self.x=20

t1=overr()
t2=overr()
print(t1.x)
print(t2.x)

class check:
    x=25

t1=check()
t2=check()
t1.x=50
print(check.x)