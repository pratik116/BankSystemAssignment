import mysql.connector as sql
import util.DBPropertyUtil as DBPropertyUtil
class DBConnUtil:
    def open(self):
        try:
            connectionString=DBPropertyUtil.DBPropertyUtil.getPropertyString()
            # print(connectionString)
            self.conn=sql.connect(user=connectionString[0],host=connectionString[1],password=connectionString[3],database=connectionString[2])
            self.stmt=self.conn.cursor()
            if self.conn.is_connected:
                print("***Database Connected***")
        except Exception as e:
            print(e)
    def close(self):
        self.conn.close()