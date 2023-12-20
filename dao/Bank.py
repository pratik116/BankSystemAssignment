import entity.Account as A
import entity.Customer as C
import entity.Transction as T
import exception.InvalidAccountException as EI
import exception.InsufficientFundException as EF
import dao.insert as I
import util.DBConnUtil as conn
DB=conn.DBConnUtil()
class Bank():
    @staticmethod
    def checkValidAccountNo(acc_no):
        try:
            DB.open()
            DB.stmt.execute(f"select * from Accounts where account_id={acc_no}")
            temp=DB.stmt.fetchall()
            if not temp:
                return False
            else:
                return True
        except Exception as e:
            print(e)
        finally:
            DB.close()
    @staticmethod
    def AddNewCustomer():
        try:
            first=input("Enter First Name: ")
            last=input("Enter Last Name: ")
            email=input("Enter Email: ")
            contno=input("Enter Contact No: ")
            location=input("Enter Location: ")
            obj=C.Customers(first,last,email,contno,location)
            I.InsertIntoTable.insertCustomer(obj)
        except Exception as e:
            print(e)

    @staticmethod
    def CreateNewAccount():
        try:
            check=input("Are you new Customer(Y/N): ")
            if(check=='Y'):
                Bank.AddNewCustomer()
                acc_type=input("Enter Account Type You Want To Open(Saving/Current): ")
                balance=int(input("Enter the balance you want to Deposite: "))
                newacc=A.Account(C.Customers.prev_CustomerID,acc_type,balance)
                I.InsertIntoTable.insertAccount(newacc)
                newTrans=T.Transaction(A.Account.prevAccountNumber,"Deposite",balance)
                I.InsertIntoTable.insertTransaction(newTrans)

            elif(check=='N'):
                Customer_id=int(input("Enter your Customer Id: "))
                acc_type=input("Enter Account Type You Want To Open(Saving/Current): ")
                balance=int(input("Enter the balance you want to Deposite: "))
                newacc=A.Account(Customer_id,acc_type,balance)
                I.InsertIntoTable.insertAccount(newacc)
                newTrans=T.Transaction(A.Account.prevAccountNumber,"Deposite",balance)
                I.InsertIntoTable.insertTransaction(newTrans)
        except Exception as e:
            print(e)

    
    @staticmethod
    def get_account_balance():
        try:
            Acc_no=int(input("Enter the Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Acc_no):
                raise EI.InvalidAccountException 
            else:
                DB.open()
                DB.stmt.execute(f"select balance from Accounts where account_id={Acc_no}")
                balance=DB.stmt.fetchone()
        except Exception as e:
            print(e)
        else:
            DB.close()
            return balance

    @staticmethod
    def depositAmount():
        try:
            Acc_no=int(input("Enter the Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Acc_no):
                raise EI.InvalidAccountException 
            else:
                Amount=int(input("Enter the amount to deposite: "))
                DB.open()
                DB.stmt.execute(f"select balance from Accounts where account_id={Acc_no}")
                oldbalance=DB.stmt.fetchone()
                Newbalance=Amount+oldbalance[0]
                DB.stmt.execute(f"update Accounts set balance={Newbalance} where account_id={Acc_no}")
                temp=DB.stmt.fetchone()
                DB.conn.commit()
                
        except EI.InvalidAccountException as e:
            print(e)
        else:
            newTrans=T.Transaction(A.Account.prevAccountNumber,"Deposite",Amount)
            I.InsertIntoTable.insertTransaction(newTrans)
            print(f"Amount Deposited Successfully\nNew Account Balance: {Newbalance}")
            DB.close()
            return temp


    @staticmethod
    def withdrawAmount():
        try:
            Acc_no=int(input("Enter the Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Acc_no):
                raise EI.InvalidAccountException 
            else:
                Amount=int(input("Enter the amount to Withdraw: "))
                DB.open()
                DB.stmt.execute(f"select balance from Accounts where account_id={Acc_no}")
                oldbalance=DB.stmt.fetchone()
                if Amount>oldbalance[0]:
                    raise EF.InsufficientFundException
                else:
                    Newbalance=oldbalance[0]-Amount
                    DB.stmt.execute(f"update Accounts set balance={Newbalance} where account_id={Acc_no}")
                    temp=DB.stmt.fetchone()
                    DB.conn.commit()
                    print(f"{Amount}/- Rupees withdrawaled from the account {Acc_no}")
                    

        except EF.InsufficientFundException as e:
            print(e)
        except EI.InvalidAccountException as e:
            print(e)
        except Exception as E:
            print(E)
        else:
            newTrans=T.Transaction(A.Account.prevAccountNumber,"Withdraw",Amount)
            I.InsertIntoTable.insertTransaction(newTrans)
            DB.close()
            return temp
        
    @staticmethod
    def calculateInterest():
        ROI=4.5
        try:
            Acc_no=int(input("Enter the Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Acc_no):
                raise EI.InvalidAccountException 
            else:
                DB.open()
                DB.stmt.execute(f"select balance from Accounts where account_id={Acc_no}")
                balance=DB.stmt.fetchone()
                interest=(ROI/100)*balance[0]
                
        except EI.InvalidAccountException as E:
            print(E)
        except Exception as E:
            print(E)
        else:
            DB.close()
            return interest
        
    @staticmethod
    def transfer():
        try:
            Sender_Acc_no=int(input("Enter Sender's Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Sender_Acc_no):
                raise EI.InvalidAccountException 
            Receiver_Acc_no=int(input("Enter Receiver's Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Receiver_Acc_no):
                raise EI.InvalidAccountException
            else:
                Amount=int(input("Enter Amount you want to Transfer: "))
                DB.open()
                DB.stmt.execute(f"select balance from Accounts where account_id={Sender_Acc_no}")
                sender_balance=DB.stmt.fetchone()
                DB.stmt.execute(f"select balance from Accounts where account_id={Receiver_Acc_no}")
                Receiver_balance=DB.stmt.fetchone()
                if Amount>sender_balance[0]:
                    raise EF.InsufficientFundException
                else:
                    New_sender_balance=sender_balance[0]-Amount
                    New_receiver_balance=Receiver_balance[0]+Amount
                    DB.stmt.execute(f"update Accounts set balance={New_sender_balance} where account_id={Sender_Acc_no}")
                    DB.conn.commit()
                    DB.stmt.execute(f"update Accounts set balance={New_receiver_balance} where account_id={Receiver_Acc_no}")
                    DB.conn.commit()
                    
        except EF.InsufficientFundException as e:
            print(e)
        except EI.InvalidAccountException as e:
            print(e)
        except Exception as E:
            print(E)
        else:
            newTrans1=T.Transaction(A.Account.prevAccountNumber,f"Transfer to{Receiver_Acc_no}",Amount)
            I.InsertIntoTable.insertTransaction(newTrans1)
            newTrans2=T.Transaction(A.Account.prevAccountNumber,f"Received from{Sender_Acc_no}",Amount)
            I.InsertIntoTable.insertTransaction(newTrans2)
            print("Transfer successful...")
            DB.close()
            
    @staticmethod
    def TransactionHistory():
        
        try:
            Acc_no=int(input("Enter the Account No: "))
            if not Bank.checkValidAccountNo(acc_no=Acc_no):
                raise EI.InvalidAccountException 
            else:
                DB.open()
                DB.stmt.execute(f"select * from transactions where account_number={Acc_no}")
                history=DB.stmt.fetchall()
                
                
        except EI.InvalidAccountException as E:
            print(E)
        except Exception as E:
            print(E)
        else:
            DB.close()
            return history

    