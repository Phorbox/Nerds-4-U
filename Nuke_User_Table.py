from distutils.command.install_lib import PYTHON_SOURCE_EXTENSION
import mysql.connector

HOST="user-information.cfe8lazrwbtc.us-east-1.rds.amazonaws.com"
USER="admin"
PASSWORD="Helpmernplz1!"
DATABASE="user"
DB = mysql.connector.connect(HOST, USER, PASSWORD, DATABASE)


USER_TABLE = "user_information"

def Drop_table():

    My_Cursor = DB.cursor()
    sql = "DROP TABLE {table}"
    sql.format(USER_TABLE)
    My_Cursor.execute(sql)

UID = "UID int NOT NULL AUTO_INCREMENT=100"
USERNAME = "Username VARCHAR(255) NOT NULL"
EMAIL = "Email VARCHAR(255) NOT NULL"
PASSWORD = "Password VARCHAR(30) NOT NULL"
FIRST = "First_Name VARCHAR(255) NOT NULL"
LAST = "Last_Name VARCHAR(255) NOT NULL"
STREET = "Address VARCHAR(255) NOT NULL"
STATE = "State CHAR(2) NOT NULL"
PHONE = "Phone CHAR(10 NOT NULL"
SCORE = "Score CHAR(2)"
PRIMARY = "PRIMARY KEY (UID)"

def Make_Table():
    My_Cursor = DB.cursor()
    sql = "Create Table {Table} ({UID}, {Username}, {Email},{Password}, {First},{Last}, {Street},{State},{Phone},{Score},{Primary})"
    sql.format(USER_TABLE,UID,          USERNAME,   EMAIL,  PASSWORD,   FIRST,  LAST,   STREET,  STATE,  PHONE,  SCORE,  PRIMARY)
    My_Cursor.execute(sql)
