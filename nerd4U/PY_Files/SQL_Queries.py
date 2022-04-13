import mysql.connector
import CONSTANTS
DB = mysql.connector.connect(host = CONSTANTS.HOST, user =  CONSTANTS.USER, password = CONSTANTS.PASSWORD, database = CONSTANTS.DATABASE)


# sql.format(USER_TABLE,UID,USERNAME,EMAIL,PASSWORD,FIRST,LAST,STREET,STATE,SCORE,PHONE,PRIMARY)
def Push_To_User_Table(Username, Email, Password, First, Last, Street, State, phone):
    My_Cursor = DB.cursor()
    sql = "insert into {} (Username,Email,pass,First_Name,Last_Name,Address,State,Phone) values  ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
    sql = sql.format(CONSTANTS.USER_TABLE,Username, Email, Password, First, Last, Street, State,phone)
    My_Cursor.execute(sql)

def Get_Email(Email):
    return Get_Any(CONSTANTS.USER_TABLE,"Email", Email)

def Get_Username(Username):
    return Get_Any(CONSTANTS.USER_TABLE,"Username", Username)

def Get_Password(Pass):
    return Get_Any(CONSTANTS.USER_TABLE,"Pass", Pass)


# Get_Any searches U
# 
# 
def Get_Any(Table, Attribute, Specifically):
    My_Cursor = DB.cursor()
    sql = "Select ({}) From {} Where ({}) = '{}'"
    sql = sql.format(Attribute,Table,Attribute,Specifically)
    My_Cursor.execute(sql)
    
    return Clean_Result(My_Cursor.fetchone())

def Clean_Result(dirty):
    return dirty[0]