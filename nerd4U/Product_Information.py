import mysql.connector

db = mysql.connector.connect(host="user-information.cfe8lazrwbtc.us-east-1.rds.amazonaws.com",
                             user="admin", password="password", database="user")

TABLE_NAME = "product_information"

#########################################
## Queries Database for products that  ##
## have specified category.            ##
#########################################


def Get_Product_By_Catagory(category):
    cursor = db.cursor()

    print(TABLE_NAME)
    print(category)

    cursor.execute(
        "SELECT * FROM product_information where catagory = '" + category + "'")
    array = cursor.fetchall()
    return (array)
