import mysql.connector

db = mysql.connector.connect(host="user-information.cfe8lazrwbtc.us-east-1.rds.amazonaws.com", user="admin",password="password",database="user")

TABLE_NAME = "user_information"


def Push_To_Database(       Username, Email, Password, First, Last, Street, State, phone):
    My_Cursor = db.cursor()
    sql = "insert into {Table_Name} values  ({Username}, {Email}, {Password}, {First}, {Last}, {Street}, {State}, {phone})"
    sql.format(TABLE_NAME,Username, Email, Password, First, Last, Street, State,phone)
    My_Cursor.execute(sql)

    
def Dupe_Name_Search(Username):
    My_Cursor = db.cursor()
    sql = "Select (Username) From {TABLE_NAME} Where (Username) Equals {Username}"
    My_Cursor.execute(sql)
    return My_Cursor.fetchone() 
def Dupe_Email_Search(Email):
    My_Cursor = db.cursor()
    sql = "Select (Username) From {TABLE_NAME} Where (Username) Equals {Email}"
    My_Cursor.execute(sql)
    return My_Cursor.fetchone()




