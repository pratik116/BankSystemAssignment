import util.DBConnUtil as conn
insert=conn.DBConnUtil()
class InsertIntoTable:
    @staticmethod
    def insertCustomer(c):
        try:
            data=[(c.get_CusID,c.get_First_Name,c.get_Last_Name,c.get_Email,c.get_Cont,c.get_address)]
            input_str='''INSERT INTO Customers (customer_id,first_name,last_name,email,phone_number,address)
                        VALUES (%s,%s,%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Customer Details Stored in database...")
    
    @staticmethod
    def insertAccount(a):
        try:
            data=[(a.get_accNo,a.get_Customer_id,a.get_type,a.get_balance)]
            input_str='''INSERT INTO Accounts (account_id,customer_id,account_type,balance)
                        VALUES (%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            print("Account Details Stored in database...")
    @staticmethod
    def insertTransaction(T):
        try:
            data=[(T.account_id,T.date_time,T.transaction_type,T.transaction_amount)]
            input_str='''INSERT INTO transactions (account_number,date_time,transaction_type,transaction_amount)
                        VALUES (%s,%s,%s,%s);
                        '''
            insert.open()
            insert.stmt.executemany(input_str,data)
            insert.conn.commit()
        except Exception as e:
            print(e)
        else:
            insert.close()
            

