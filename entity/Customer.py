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

    @property
    def get_CusID(self):
        return self._CusID
    @property
    def get_First_Name(self):
        return self._First_Name
    @property
    def get_Last_Name(self):
        return self._Last_Name
    @property
    def get_Email(self):
        return self._Email
    @property
    def get_Cont(self):
        return self._Cont
    @property
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