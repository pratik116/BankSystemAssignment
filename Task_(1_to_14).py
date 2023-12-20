# Banking System Assignment 
# Control Structure
# Task 1: Conditional Statements
'''
creditScore=int(input("Enter Credit Score: "))
annualIncome=int(input("Enter Annual Income: "))
if(creditScore<300 or creditScore>900):
    print("Please enter valid Credit Score")
elif(creditScore>700 and annualIncome<=50000):
    print("The Customer is eligible for loan")
else:
    print("The Customer is not eligible for loan")


# Task 2: Nested Conditional Statements

try:
    currBalance=int(input("Enter Current Balance: "))
    operation=input("For Check Balance press 'C'\nFor Deposite press 'D'\nFor Withdraw press 'W'\n")
    if(operation=='C'):
        print(f"Current Balance: {currBalance}")
    elif(operation=='D'):
        deposite=int(input("Enter amount to Deposite: "))
        currBalance+=deposite
        print(f"Current Balance: {currBalance}")
    else:
        withdraw=int(input("Enter amount to Deposite: "))
        if(withdraw%100!=0):
            print("Withdrawal amount must be multiple of 100")
        elif(withdraw<=currBalance):
            currBalance-=withdraw
            print(f"Current Balance: {currBalance}")
        else:
            print("Insufficient Balance")
except Exception as e:
    print(e)


# Task 3: Loop Structure

nc=int(input("Enter the total number of Account holders: "))
for i in range(0,nc):
    currBal=int(input(f"Enter Current Balance of {i+1}th Holder: "))
    AIR=int(input("Enter Annual Interest Rate: "))
    Years=int(input("Enter number of Years: "))
    futureBalance=format(currBal*pow((1+(AIR/100)),Years),'.2f')
    print(f"Balance after {Years} Years: {futureBalance}")



# Task 4: Looping, Array and Data Validation

BankBalances={}
try: 
    N=int(input("Enter the total number of Account holders: "))
    for i in range(0,N):
        currBal1=int(input(f"Enter Current Balance of {i+1}th Holder: "))
        BankBalances.update({100+i:currBal1})
    check='Y'
    while(check=='Y'):
        Accno=int(input("Enter Account Number: "))
        if Accno in BankBalances.keys():
            print(f"Current Balance of {Accno}: {BankBalances[Accno]}")
        else:
            print("Please enter valid Account Number")
            continue
        check=input("Want to Continue: (Y/N): ")   
except Exception as e:
    print(e)


# Task 5: Password validation
flag1=0
flag2=0
while(flag1==0 and flag2==0):
    try:
        password=input("Enter a Password: ")
        if(len(password)>=8):
            for i in password:
                if(flag1==0 and (ord(i)>=48 or ord(i)<=57)):
                    flag1=1
                elif(flag2==0 and (ord(i)>=65 or ord(i)<=90)):
                    flag2=1
                if(flag1 and flag2):
                    print("Valid Password")
                    break
            print("invalid password please try again")
            flag1=0 
            flag2=0
            continue
        else:
            print("invalid password please try again")
    except Exception as e:
        print(e)

# Task 6: Transaction History

History=[]
check="Y"
while(check=="Y"):
    operation=input("For Deposite press 'D'\nFor Withdraw press 'W'\n")
    if(operation=="D"):
        deposite=int(input("Enter amount to Deposite: "))
        History.append(f"{deposite}/- RS Deposited")
    elif(operation=="W"):
        withdraw=int(input("Enter amount to Deposite: "))
        History.append(f"{withdraw}/- RS Withdrawaled")
    else:
        print("Enter valid Operation")
    check=input("Want to Continue: (Y/N): ")   
print(History)

'''
'''
# Task 7: Class & Object

# Task 7.1: Create a `Customer` class with the following confidential attributes:
class Customers:
    def __init__(self,CusID,First_Name,Last_Name,Email,Cont,Address):
        self._CusID=CusID
        self._First_Name=First_Name
        self._Last_Name=Last_Name
        self._Email=Email
        self._Cont=Cont
        self._Address=Address
    
    def get_CusID(self):
        return self._CusID

    def get_First_Name(self):
        return self._First_Name

    def get_Last_Name(self):
        return self._Last_Name

    def get_Email(self):
        return self._Email

    def get_Cont(self):
        return self._Cont
    
    def get_address(self):
        return self._Address

    
    def copyObject(self,Customers):
        self._CusID=Customers.get_CusID
        self._First_Name=Customers.get_Last_Name
        self._Last_Name=Customers.get_Last_Name
        self._Email=Customers.get_Email
        self._Cont=Customers.get_Cont
        self._Address=Customers.get_address

    def set_CusID(self,CusID):
        self_CusID=CusID

    def set_First_Name(self,First_Name):
        self_First_Name=First_Name

    def set_Last_Name(self,Last_Name):
        self_Last_Name=Last_Name

    def set_Email(self,Email):
        self_Email=Email

    def set_Cont(self,Cont):
        self_Cont=Cont

    def set_address(self,Address):
        self_Address=Address

    
    def printCustomerInfo(self):
        print("Customer ID:",self._CusID)
        print("First Name:",self._First_Name)
        print("Last Name:",self._Last_Name)
        print("Email:",self._Email)
        print("Contact Number:",self._Cont)
        print("Address:",self._Address)

# Task 7.2: Create an `Account` class with the following confidential attributes:
class Account:
    def __init__(self,accNo,type,balance):
        self._accNo=accNo
        self._type=type
        self._balance=balance
        self._accHistory=[]
    
    def get_accNo(self):
        return self._accNo

    def get_type(self):
        return self._type

    def get_balance(self):
        return self._balance

    
    def set_accNo(self,accNo):
        self._accNo=accNo

    def set_type(self,type):
        self._type=type

    def set_balance(self,balance):
        self._balance=balance


    def printAccountInfo(self):
        print("Account Number:",self._accNo)
        print("Account Type:",self._type)
        print("Account Balance:",self._balance)

    def depositAmount(self, depositAmount):
        self._balance+=depositAmount
        print(f"{depositAmount}/- Rupees deposited into the account {self._accNo}")
    
    def withdrawAmount(self, withdrawAmount):
        if withdrawAmount<=self._balance:
            self._balance-=withdrawAmount
            print(f"{withdrawAmount}/- Rupees withdrawaled from the account {self._accNo}")
        else:
            print("Insufficient balance..")

    def calculateInterest(self):
        ROI=4.5
        interest=(ROI / 100)*self._balance
        print(f"Interest: {interest}")

# Task 7.3: 

Cust1=Customers(101,'Pratik','Wani','pratik@gmail.com','9002002110','Nashik')
Cust1.printCustomerInfo()
print("\n")
Acc1=Account(1001,'Saving Account',24000)
Acc1.printAccountInfo()

Acc1.depositAmount(300.123)

Acc1.withdrawAmount(1001.45)

print(Acc1.get_balance())

Acc1.calculateInterest()

# Task 8: Inheritance and polymorphism
 
# Task 8.1)  In pythons int,float data types are handled automatically so we dont need to overload the deposite and withdraw methonds
# for int, float data types

# Task 8.2) Create Subclasses for Specific Account Types

class SavingsAccount(Account):
    def __init__(self,accNo,balance,ROI_saving):
        super().__init__(accNo=accNo,type="Savings",balance=balance)
        self._ROI_saving=ROI_saving

    def calculate_interest(self):
        interest=(self._ROI_saving/100)*self._balance
        print(f"Interest for Savings Account: {interest}")

class CurrentAccount(Account):

    def __init__(self,accNo,balance,ODLimit):
        super().__init__(accNo=accNo,type="Current",balance=balance)
        self._ODLimit=ODLimit

    def withdraw(self,withdrawAmount):
        if(withdrawAmount<self._balance):
            super().withdrawAmount(withdrawAmount)
        else:
            total_balance=self._balance+self._ODLimit
            try:
                if withdrawAmount<=total_balance:
                    self._balance-=withdrawAmount
                    print(f"{withdrawAmount}/- Rupees withdrawaled from the account {self._accNo}\nOverDraft Limit Remaining: {self._ODLimit+self._balance}")
                else:
                    raise Exception(OverDraftLimitExcededException)
            except Exception as e:
                print(e)


# Task 8.3: 


AccType=input("Welcome!! Please Enter the type of account you want to open\nPress 'S' for Saving Account\nPress 'C' for Current Account\n " )

if(AccType=='C'):
        CurrentAccount1=CurrentAccount(1002,5000,5000)
        Operation=5
        while(Operation!=0):
            try:
                Operation=int(input("1) press 1 for Deposit\n2) press 2 for Withdrawal\n3) press 3 to calculate intrest\n4) press 0 to exit\n"))
                if(Operation==1):
                    amount=int(input("Enter the amount to deposit: "))
                    CurrentAccount1.depositAmount(amount)
                elif(Operation==2):
                    amount=int(input("Enter the amount to withdraw: "))
                    CurrentAccount1.withdrawAmount(amount)
                elif(Operation==3):
                    CurrentAccount1.calculateInterest()
                elif(Operation==0):
                    print("Thank you!!")
                    break
                else:
                    print("Please select correct option..")
            except Exception as e:
                print(e)



elif(AccType=='S'):
        SavingsAccount1=SavingsAccount(1002,5000,11)

        Operation=5
        while(Operation!=0):
            try:
                Operation=int(input("1) press 1 for Deposit\n2) press 2 for Withdrawal\n3) press 3 to calculate intrest\n4) press 0 to exit\n"))
                if(Operation==1):
                    amount=int(input("Enter the amount to deposit: "))
                    SavingsAccount1.depositAmount(amount)
                elif(Operation==2):
                    amount=int(input("Enter the amount to withdraw: "))
                    SavingsAccount1.withdrawAmount(amount)
                elif(Operation==3):
                    SavingsAccount1.calculateInterest()
                elif(Operation==0):
                    print("Thank you!!")
                    break
                else:
                    print("Please select correct option..")
            except Exception as e:
                print(e)


else:
    print("Please select correct option..")

'''

# Task 9: Abstraction is not concept of python

# Task 10 & 12: Association + Exception Handling

class Customers:
    prev_CustomerID=0
    def __init__(self,First_Name,Last_Name,Email,Cont,Address):
        self._CusID=Customers.prev_CustomerID+1
        Customers.prev_CustomerID+=1
        self._First_Name=First_Name
        self._Last_Name=Last_Name
        self._Email=Email
        self._Cont=Cont
        self._Address=Address
    
    def get_CusID(self):
        return self._CusID

    def get_First_Name(self):
        return self._First_Name

    def get_Last_Name(self):
        return self._Last_Name

    def get_Email(self):
        return self._Email

    def get_Cont(self):
        return self._Cont
    
    def get_address(self):
        return self._Address

    
    def copyObject(self,Customers):
        self._CusID=Customers.get_CusID
        self._First_Name=Customers.get_Last_Name
        self._Last_Name=Customers.get_Last_Name
        self._Email=Customers.get_Email
        self._Cont=Customers.get_Cont
        self._Address=Customers.get_address

    def set_CusID(self,CusID):
        self_CusID=CusID

    def set_First_Name(self,First_Name):
        self_First_Name=First_Name

    def set_Last_Name(self,Last_Name):
        self_Last_Name=Last_Name

    def set_Email(self,Email):
        self_Email=Email

    def set_Cont(self,Cont):
        self_Cont=Cont

    def set_address(self,Address):
        self_Address=Address

    
    def printCustomerInfo(self):
        print("Customer ID:",self._CusID)
        print("First Name:",self._First_Name)
        print("Last Name:",self._Last_Name)
        print("Email:",self._Email)
        print("Contact Number:",self._Cont)
        print("Address:",self._Address)

class Account:
    prevAccountNumber = 1000

    def __init__(self,Customers,type,balance):
        self.Customer=Customers
        self._accNo=Account.prevAccountNumber+1
        Account.prevAccountNumber=self._accNo
        self._type=type
        self._balance=balance

    
    def get_accNo(self):
        return self._accNo

    def get_type(self):
        return self._type

    def get_balance(self):
        return self._balance

    
    def set_accNo(self,accNo):
        self._accNo=accNo

    def set_type(self,type):
        self._type=type

    def set_balance(self,balance):
        self._balance=balance


    def printAccountInfo(self):
        print("Account Number:",self._accNo)
        print("Account Type:",self._type)
        print("Account Balance:",self._balance)

    def depositAmount(self, depositAmount):
        self._balance+=depositAmount
        print(f"{depositAmount}/- Rupees deposited into the account {self._accNo}")
    
    def withdrawAmount(self,withdrawAmount):
        if withdrawAmount<=self._balance:
            self._balance-=withdrawAmount
            print(f"{withdrawAmount}/- Rupees withdrawaled from the account {self._accNo}")
        else:
            print("Insufficient balance..")

    def calculateInterest(self):
        ROI=4.5
        interest=(ROI / 100)*self._balance
        print(f"Interest: {interest}")


#exceptions 

class InsufficientFundException(Exception):
    def __init__(self):
        super().__init__("InsufficientFundException")
    
class InvalidAccountException(Exception):
    def __init__(self):
        super().__init__("InvalidAccountException") 

#implimention of bank

class Bank:
    def __init__(self):

        self.bankaccounts={}

    def create_account(self,Customers,type,balance):        
            account=Account(Customers,type,balance)
            self.bankaccounts[account.get_accNo()]=account
            print("Account created successfully... Account Number: ",account.get_accNo())

    def get_account_balance(self,accNo):
        try:
            if accNo in self.bankaccounts:
                return self.bankaccounts[accNo].get_accNo()
            else:
                raise Exception("InvalidAccountException") # Task 12 exception handling
        except Exception as e:
            print(e)
            

    def deposit(self,accNo,amount):
        try:
            if accNo in self.bankaccounts:
                account=self.bankaccounts[accNo]
                account.depositAmount(amount)
            else:
                raise Exception("InvalidAccountException") # Task 12 exception handling
        except Exception as e:
            print(e)

    def withdraw(self,accNo,amount):
        try:
            if accNo in self.bankaccounts:
                account=self.bankaccounts[accNo]
                account.withdrawAmount(amount)
            else:
                raise Exception("InvalidAccountException") # Task 12 exception handling
        except Exception as e:
            print(e)
            

    def transfer(self,from_accNo,to_accNo,amount):
        if from_accNo in self.bankaccounts and to_accNo in self.bankaccounts:
            fromacc=self.bankaccounts[from_accNo]
            toacc=self.bankaccounts[to_accNo]
            try:
                if fromacc.get_accNo()>=amount:
                    fromacc.withdrawAmount(amount)
                    toacc.depositAmount(amount)
                    print("Transfer successful...")
                else:
                    raise Exception("InsufficientFundException") # Task 12 exception handling
            except Exception as e:
                print(e)
        else:
            print("Account no found..")

    def get_account_details(self,accNo):
        if accNo in self.bankaccounts:
            account=self.bankaccounts[accNo]
            account.printAccountInfo()
        else:
            print("Account not found.")





bank=Bank()

customer1=Customers(101,"Pratik","Wani","pratik@gmail.com","9900221122","Nashik")
customer2=Customers(102,"Vikas","Thakre","vikas@gmail.com","9900222345","Pune")


bank.create_account(customer1,"Savings",5000.0)
bank.create_account(customer2,"Current",6000.0)

bank.deposit(1001,4000)
bank.withdraw(1002,80000)
bank.withdraw(1002,500)
bank.transfer(1001,1002,500)

bank.get_account_details(1001)
bank.get_account_details(1002)

# Task 13: Collection is not concept of python

# Task 14: DB connect performed in Base Folder 