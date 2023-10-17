import bank as bnk
class Fixed_deposite_ac(bnk.Bank):
    '''
    A fixed deposit (FD) account is a secure investment that offers guaranteed returns. FDs have the following features
    '''
    FD_roi=7.5

    def __init__(self,amount,time):
        self.amount=amount
        self.time=time
        print(f"Amount deposited in FD is Rs.{amount}")
        super().__init__(amount)
    
    def interest(self, time):
        print("==============Interest================")
        if time<=0:
            print("insterest cannot be calculated")
        Amount =self.amount * (pow((1 + self.FD_roi/100), time))
        CI = Amount - self.amount
        print(f"compounded interest on current money over {time} month will be Rs.{CI} ")
    
    def withdraw(self,amount,time):
        print("==============Withdraw================")
        if amount>=self.amount:
            print("you cant withdraw over the amount you have")
        if time<=self.time:
            print("you cant withdraw Before the fixed time")
        else:
            print( f"Amount {amount} is withdrawed from your Bank account")
            self.amount-=amount
            print( f"Current Balance in Account is {self.amount}")
    def __str__(self) :
        print("==============Our Interset In Fixed Deposites================")
        return f"Rate of Interest in Bank is {self.FD_roi}"
class Savings_ac(bnk.Bank):

    def __init__(self,money):
        print("==============Amount================")
        self.amount=money
        print(f"amount of money ={self.amount}")
        
    def withdraw(self,amount):
        print("==============Withdraw================")
        if amount>=self.amount:
            print("you cant withdraw")
        else:
            print( f"Amount {amount} is withdrawed from your Bank account")
            self.amount-=amount
            print( f"Current Balance in Account is {self.amount}")

    def deposite(self,amount):
        print("==============Deposite================")
        if amount<=0:
            print("you cant deposite")
        else:
            print( f"Amount {amount} is deposited in your Bank account")
            self.amount+=amount
            print( f"Current Balance in Account is {self.amount}")
            # return self.amount

    def interest(self,time):
        print("==============Interest================")
        if time<=0:
            print("insterest cannot be calculated")
        else:
            if time<=0:
                print("insterest cannot be calculated")
            Amount =self.amount * (pow((1 + bnk.Bank.rate_of_interest/100), time))
            CI = Amount - self.amount
            print(f"compounded interest on current money over {time} month will be Rs.{CI} ")

    def __str__(self) :
        print("==============Our Interset in Savings================")
        return f"Rate of Interest in Bank is {bnk.Bank.rate_of_interest}"



if __name__ == "__main__":
    o1=Fixed_deposite_ac(200,12)
    print(o1)
    print(o1.withdraw(200,10))
    print(o1.interest(10))
    o2=bnk.Bank(200)
    print(o2.interest(10))

    o3=Savings_ac(900)
    print(o3.interest(10))