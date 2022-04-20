import mysql.connector
from PY_Files import CONSTANTS
DB = mysql.connector.connect(host=CONSTANTS.HOST, user=CONSTANTS.USER,
                             password=CONSTANTS.PASSWORD, database=CONSTANTS.DATABASE)


# sql.format(USER_TABLE,UID,USERNAME,EMAIL,PASSWORD,FIRST,LAST,STREET,STATE,SCORE,PHONE,PRIMARY)
def Push_To_User_Table(Username, Email, Password, First, Last, Street, State, phone):
    My_Cursor = DB.cursor()
    sql = "insert into {} (Username,Email,pass,First_Name,Last_Name,Address,State,Phone) values  ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
    sql = sql.format(CONSTANTS.USER_TABLE, Username, Email,
                     Password, First, Last, Street, State, phone)
    My_Cursor.execute(sql)




def Get_Email(Email):
    return Select_Any(CONSTANTS.USER_TABLE, "Email", ["Email"], [Email])


def Get_Username(Username):
    return Select_Any(CONSTANTS.USER_TABLE, "Username", ["Username"], [Username])


def Get_Password(Pass):
    return Select_Any(CONSTANTS.USER_TABLE, "Pass", ["Pass"], [Pass])



def Get_Login(UserInfo):
    return Select_Any(CONSTANTS.USER_TABLE, "UID", ["Username","Pass"], UserInfo)


# Get_Any searches U
#
#
def Select_Any(Table, Select_List, Attribute_List, Value_List):
    My_Cursor = DB.cursor()
    sql = "Select ({}) From {} Where {}"
    Where = Format_Where_Statement(Attribute_List, Value_List)
    sql = sql.format(Select_List, Table, Where)
    print(sql)
    My_Cursor.execute(sql)
    


    return Clean_Result(My_Cursor.fetchone())


def Clean_Result(dirty):
    print(dirty)
    if(dirty == None):
        return "none"
    return dirty[0]


def Format_Where_Statement(Attribute_List, Value_List):
    sql = "({}) = '{}'"
    returner = ""

    for x, y in zip(Attribute_List, Value_List):
        returner += sql.format(x, y)
        returner += " AND "

    returner = returner[:-len(" AND ")]
    return (returner)
