class Vehicle:
    type=brand=model='x'
    
    def __init__(self,type,brand,model,bt):
        Vehicle.type=type
        Vehicle.brand=brand
        Vehicle.model=model
        self.body_type=bt
        print("Calling Constructor from Vehicle class:",Vehicle.type)

    def func1(self):
        print("Calling from Vehicle class")
        print(f'The brand of the {Vehicle.type} is {Vehicle.brand}')
        print(f'The model is {Vehicle.model} and body type is {self.body_type}')

class Brand(Vehicle):

    segment=''

    def func2(self,sgm):
        if len(sgm)>0:
            Brand.segment=sgm
        #print("Vahicle Segment is:")
        print(f"Calling function from Brand function for {Vehicle.model} and Segment is:{Brand.segment}")
       
    def change_req(self,brand,model):
        Vehicle.brand=brand
        Vehicle.model=model
        print("Changes successful")


class Model(Brand):

    def func3(self,clr):
        self.color=clr
        print("Calling function from Model")
        print(f"Color of the {Vehicle.model} is: {self.color}")

    def need_chgs(self): #Shouldn't call this method as Has-a cannot be combined in inheritance without using super()
        #Hardcoding parent name is not good for multiple inheritance so 
        # avoid Brand.change_reg('Audi','Q5)
        self.brandobj=Brand() #doesn't work as no constructor in Brand class
        self.brandobj.change_req('Infiniti','QX80')

    def prn_chgs(self):
        print(f'The brand of the {Vehicle.type} is {Vehicle.brand}')
        print(f'The model is {Vehicle.model} and color is {self.color}')


Model_obj=Model('Car','Lexus','GX350','SUV')
Model_obj.func1()
Model_obj.func2('Luxury')
print("The Car segment is:",Brand.segment)
Model_obj.func3('Black')
Model_obj.change_req('BMW','d750i')
Model_obj.prn_chgs()