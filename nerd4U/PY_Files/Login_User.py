from PY_Files import SQL_Queries


def Login_User(Username, Password):
    
    return SQL_Queries.Get_Login([Username,Password])

