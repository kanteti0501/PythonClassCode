class Bankact:
    bank_name='Bank Of America'
    def __init__(self,name,accountno):
        self.name=name
        self.actnum=accountno

    def prn_det(self):
        print('Bank name:',self.bank_name)
        print('Bank name and account number: ',self.name,self.actnum)

    @classmethod
    def changebank(cls,b_name):
        cls.bank_name=b_name

    @staticmethod
    def is_valid_amt(amount):
        return amount > 0
    
bobj=Bankact('Kiran','1234567')
bobj.prn_det()
Bankact.changebank('Chase')
Bankact.is_valid_amt(1000)
bobj.prn_det()

class Engine:
    def start(self):
        print(" Engine is started")

class Car:
    def __init__(self):
        self.eobj=Engine()

    def start_engine(self):
        self.eobj.start()

cobj=Car()
cobj.start_engine()