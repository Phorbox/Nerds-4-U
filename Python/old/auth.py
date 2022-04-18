from Log_auth import Auth_Key
from user import user


# Auth_Sql_Test returns
#  userId for valid login
#  -1 for invalid login
def Auth_Sql_Test(I_Name,I_Pass):
    key = Auth_Key(I_Name)
    
    if (I_Name != key.User_Name or I_Pass != key.Pass):    
        return -1
    else: 
        return key.UID

def Create_User(Email,Password,Second,First, Last, Street, State):
    # need a username parameter for Create_User
    Verify_User_Name()

def Verify_User_Name(Check_User):
    if My_Sql_Check_Dupe_User(Check_User):
        return False
    else:
        return True