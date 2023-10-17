class Bank:
    """
	This is Bank
	A user can have an account in Bank
    user can Deposite,withdraw money 
    user also can see interest over the time on the money they have in their ac
	"""

    rate_of_interest=6.5

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
            print( f"Current Balance in Account is {self.amount}")
            money_with_interest=(self.amount*(time/12)*Bank.rate_of_interest)/100
            print(f"Simple interest on current money over {time} month will be Rs.{money_with_interest} ")

    def __str__(self) :
        print("==============Our Interset================")
        return f"Rate of Interest in Bank is {Bank.rate_of_interest}"


if __name__ == "__main__":
    initial=int(input("Deposite Rs. 500 to open your account"))
    user=Bank(initial)
    operation=1
    while operation:
        o=int(input("Enter 1 withdraw 2 deposite 3 interest"))
        if o==1:
            a=int(input("Enter amount you want to withdraw"))
            user.withdraw(a)
        if o==2:
            b=int(input("Enter amount you want to withdraw"))
            user.deposite(b)
        if o==3:
            c=int(input("Enter no. of months you want to see the interest over the time"))
            user.interest(c)
        else :
            print("Enter a valid operation")

        operation=int(input("Enter 0 to exit the bank \n Enter 1 to do some operation in the bank"))
    