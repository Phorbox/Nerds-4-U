import mysql.connector
from PY_Files import CONSTANTS
DB = mysql.connector.connect(host=CONSTANTS.HOST, user=CONSTANTS.USER,
                             password=CONSTANTS.PASSWORD, database=CONSTANTS.DATABASE)

U_TABLE = CONSTANTS.USER_TABLE
P_TABLE = CONSTANTS.PROD_TABLE

# sql.format(USER_TABLE,UID,USERNAME,EMAIL,PASSWORD,FIRST,LAST,STREET,STATE,SCORE,PHONE,PRIMARY)
def Push_To_User_Table(Username, Email, Password, First, Last, Street, State, phone):
    My_Cursor = DB.cursor()
    sql = "insert into {} (Username,Email,pass,First_Name,Last_Name,Address,State,Phone) values  ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')"
    sql = sql.format(U_TABLE, Username, Email,
                     Password, First, Last, Street, State, phone)
    My_Cursor.execute(sql)
    DB.commit()


def Get_Email(Email):
    return Select_Any(U_TABLE, "Email", ["Email"], [Email])


def Get_Username(Username):
    return Select_Any(U_TABLE, "Username", ["Username"], [Username])


def Get_Password(Pass):
    return Select_Any(U_TABLE, "Pass", ["Pass"], [Pass])



def Get_Login(UserInfo):
    return Select_Any(U_TABLE, "UID", ["(Username)","(Pass)"], UserInfo)

def Get_Cart(UID):
    return Select_Any(U_TABLE, "Cart", ["UID"], [UID])


# Get_Any searches U
#
#
def Select_Any(Table, Select_List, Attribute_List, Value_List):
    My_Cursor = DB.cursor()
    sql = "Select ({}) From {} Where {}"
    Where = Format_Zip_List(Attribute_List, Value_List,"And")
    sql = sql.format(Select_List, Table, Where)
    print (sql)
    My_Cursor.execute(sql)
    returner = My_Cursor.fetchone()
    # My_Cursor.close()
    return Clean_Result(returner)


def Clean_Result(dirty):
    if(dirty == None):
        return "none"
    return dirty[0]

# 
# 
# 
# 
# 

def Format_Zip_List(Attribute_List, Value_List,Delimiter):
    sql = "{} = '{}'"
    returner = ""
    True_Delimiter = " {} ".format(Delimiter)

    for x, y in zip(Attribute_List, Value_List):
        returner += sql.format(x, y)
        returner += True_Delimiter

    returner = returner[:-len(True_Delimiter)]
    return (returner)

def Format_Single_List(List,Delimiter):
    sql = "{}"
    Returner = ""
    True_Delimiter = " {} ".format(Delimiter)

    for x in List:
        Returner += sql.format(x)
        Returner += True_Delimiter

    Returner = Returner[:-len(True_Delimiter)]
    return (Returner)


def Update_Field(Table,Attribute_List, Value_List, ID_Type,ID):
    My_Cursor = DB.cursor()
    update = "update {}".format(Table)
    set = "set " + Format_Zip_List([Attribute_List], [Value_List],",")
    where = "Where {} = {}".format(ID_Type,ID)
    sql  = "{} {} {}".format(update,set,where)
    My_Cursor.execute(sql)
    DB.commit()

def UserIdToUsername(uid):
    My_Cursor = DB.cursor()
    My_Cursor.execute(("SELECT * FROM user_information where UID = {} ".format(uid)))
    user = My_Cursor.fetchone()
    return (user)

