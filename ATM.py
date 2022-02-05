class Atm(object):
    def __init__(self,atmCardNum,pinNum,balance):
        self.atmCardNum = atmCardNum
        self.pinNum = pinNum
        self.balance = balance
    
    def withdraw(self,ammount):
        if self.balance >= ammount:
            self.balance = self.balance - ammount
            print("ammount debited :"+ str(ammount))
            print("balance remaining :"+str(self.balance))
        else :
            print("You dont have enough balance!!")

    def checkBalance(self):
        print(str(self.balance))

    def depositMoney(self,ammount):
        self.balance = self.balance + ammount
        print("ammount deposited :"+ str(ammount))
        print("New balance :"+str(self.balance))

# creating object from the class
Mohan = Atm(224422 , 885588 , 5000)
Liz = Atm(442221 , 445544 , 8000)

#Using Functions
Mohan.checkBalance()
Liz.withdraw(5000)
Mohan.withdraw(10000)
Mohan.depositMoney(10000)