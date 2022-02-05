class Atm(object):
    def __init__(self,atmCardNum,pinNum,balance):
        self.atmCardNum = atmCardNum
        self.pinNum = pinNum
        self.balance = balance
    
    def withdraw(self,ammount):
        if self.balance >= ammount:
            pin = int(input("Enter card pin number to withdraw:"))
            if pin == int(self.pinNum):
                self.balance = self.balance - ammount
                print("ammount debited :"+ str(ammount))
                print("balance remaining :"+str(self.balance))
            elif pin != int(self.pinNum):
                print("Wrong Pin ")
        else :
            print("You dont have enough balance!!")

    def checkBalance(self):
        pin = int(input("Enter card pin number to check balance:"))
        if pin == int(self.pinNum):
            print(str(self.balance))
        elif pin != int(self.pinNum):
            print("Wrong Pin")
           
    def depositMoney(self,ammount):
        pin = int(input("Enter card pin number to deposit:"))
        if pin == int(self.pinNum):
            self.balance = self.balance + ammount
            print("ammount deposited :"+ str(ammount))
            print("New balance :"+str(self.balance))
        elif pin != int(self.pinNum):
            print("Wrong Pin ")

# creating object from the class
Mohan = Atm(224422 , 885588 , 5000)
Liz = Atm(442221 , 445544 , 8000)

#Using Functions use pins Mohan = 885588 and Liz = 445544
Mohan.checkBalance()
#Liz.withdraw(5000) 
#Mohan.withdraw(10000)
#Mohan.depositMoney(10000)