import dao.Bank as B

def main():

    while True:
        try:
            print("\n****Welcome User*****\n")
            print("Press 1 to Add New Customer")
            print("Press 2 to Create New Account")
            print("Press 3 to Check Account Balance")
            print("Press 4 to Deposite Money")
            print("Press 5 to Withdraw Money")
            print("Press 6 to Transfer Money")
            print("Press 7 to Calculate Intrest")
            print("Press 8 to View Transctions")
            print("Press 9 to Exit")

            check = int(input("Enter Here: "))
            if check==1:
                B.Bank.AddNewCustomer()

            elif check==2:
                B.Bank.CreateNewAccount()

            elif check==3:
                balance=B.Bank.get_account_balance()
                print("Account Balance: ",balance[0])

            elif check==4:
                B.Bank.depositAmount()
                

            elif check==5:
                B.Bank.withdrawAmount()
            
            elif check==6:
                B.Bank.transfer()

            elif check==7:
                Interest=B.Bank.calculateInterest()
                print("Interest Amount: ",Interest)

            elif check==8:
                History=B.Bank.TransactionHistory()
                for i in History:
                    print(i)

            elif check==9:
                print("Thank You User!!")
                break
            else:
                print("\nInvalid Option")
        except Exception as e:
            print(e)
if __name__=='__main__':
    main()