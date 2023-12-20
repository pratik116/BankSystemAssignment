import unittest
import util.DBConnUtil as DB
import dao.Bank as B
import entity.Account as A
temp=DB.DBConnUtil()
class TestCreateAccpunt(unittest.TestCase):
    def testCreateAccountmethod(self):
        temp.open()
        B.Bank.CreateNewAccount()
        prev=A.Account.prevAccountNumber
        temp.stmt.execute(f"SELECT * FROM Accounts WHERE account_id={prev}")
        result=temp.stmt.fetchone()
        self.assertEqual(result[0],prev)
    
    
    def tearDown(self):
        temp.close()

if __name__ == '__main__':
    unittest.main()
