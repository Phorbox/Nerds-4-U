import Create_User_SQL

# sql.format(USER_TABLE,UID,USERNAME,EMAIL,PASSWORD,FIRST,LAST,STREET,STATE,SCORE,PHONE,PRIMARY)
def Create_User(Username, Email, Password, First, Last, Street, State, Phone):
    print("in user")
    Dupe_Code = Verify_Duplicate(Username,Email)
    if (Dupe_Code != 0):
        Return = Will_Return_Statement(Dupe_Code)
    Create_User_SQL.Push_To_Database(Username, Email, Password, First, Last, Street, State,Phone)

# Returns a string from a Dupe code
def Will_Return_Statement(Dupe_Code):
    if (Dupe_Code == 1):
        Dupe_Statement = "That Username is already in use"
    if (Dupe_Code == 2):
        Dupe_Statement = "That Email Address is already in use"
    if (Dupe_Code == 3):
        Dupe_Statement = "That Username and Email Address is already in use"
    return Dupe_Statement


# Verify_Duplicate returns an int code of possible duplication
# 0 is no dupe
# 1 is dupe Name
# 2 is dupe Email
# 3 is dupe Both
# 
def Verify_Duplicate(Username,Email):
    
    Temp_SQL_Results = Run_Dupe_SQL_Search(Username,Email)
    Dupe_Code = 0

    if(Username == Temp_SQL_Results[0]):
        Dupe_Code +=1
    if(Email == Temp_SQL_Results[1]):
        Dupe_Code +=2

    return Dupe_Code

def Run_Dupe_SQL_Search(Username,Email):
    a = Create_User_SQL.Dupe_Name_Search(Username)
    b = Create_User_SQL.Dupe_Email_Search(Email)
    return [a,b]