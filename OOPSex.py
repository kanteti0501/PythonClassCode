class Sample:

    def __init__(self,name,age=30):
        self.name=name
        self.age=age
    
    def sample1(self):
        print("Welcome")


#Samobj=Sample()
Samobj=Sample('Kiran',42)
print("Name =",Samobj.name)
print("Age=",Samobj.age)
Samobj.sample1()
print(Samobj)
s2=Sample("Priya")

# Organise code, reuse code, easier to manage large programs

class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def bark(self):
        print(self.name," says Woof!")

    def mydoggy(self):
        
        mesg=self.greet()
        print(mesg)
        print(f"{self.name},{self.age}")

    def greet(self):
        return "hellooo" + self.name


d1=Dog("Buddy",3)
d1.bark()
d1.mydoggy()
d1.age=5
d1.mydoggy()

class Person:
    def __init__(self,name,address,phone):
        self.name=name
        self.address=address
        self.phone=phone

    def __str__(self):
        return f"({self.name} {self.address} {self.phone})"
    
p1=Person("Kiran","3029  Straight Arrow","9008764432")
print(p1)
