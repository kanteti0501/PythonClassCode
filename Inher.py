class Sample:
    @staticmethod
    def func():
        print("This is function from Sample class")


class Test():
    def __init__(self):
        gobj = Sample()
        gobj.func()


objSample = Sample()
objTest = Test()
#objTest.getfn()
print(type(objSample))

class Vehicle:
    color='blue'
    def __init__(self,name,model,brandname):
        self.name=name
        self.model=model
        self.brand=brandname
        print("NAme of the car is:",self.name)

    def func1(self):
        print("Calling from Vehicle class",self.color)

class Model(Vehicle):
    type1='Sedan'

    def func2(self):
        print("Vahicle model is:",self.model)
        print("Calling function from Model for type",self.type1)

class Brand(Model):
    label='Mycar'

    def func3(self):
        print("Vahicle Brand is:",self.name)
        print("Calling function from Brand function for type",self.label)  

#objv=Vehicle('Car','E350','Benz')
#objm=Model('Car','E350','Benz')
objb=Brand('Car','E350','Benz')   
objb.func1()  
objb.func2()
#objm.func1()
objb.func3()
objb.label='PathFinder'
print("Changed label to ",objb.label)

