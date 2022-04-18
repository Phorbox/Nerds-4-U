from PY_Files import SQL_Queries

def Login_User(Username,Password):
    if(not(Check_Username(Username))):
        return "Invalid Username"
    
    if(not(Check_Password(Password))):
        return "Invalid Password"
    
    

def Check_Username(Username):
    return Username == SQL_Queries.Get_Username(Username)
    
def Check_Password(Password):
    return Password == SQL_Queries.Get_Password(Password)

