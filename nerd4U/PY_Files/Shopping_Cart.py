# session id -> UID
# UID -> Shopping Cart lsit(as a string)
# convert string to list of Pid
# get Select pids
# paste pids into cart
from PY_Files import SQL_Queries, REGEX
from PY_Files import CONSTANTS

def Add_To_Cart(UID,New_PID):
    Temp_Cart = Pull_Cart(UID)
    Temp_Cart = Add_Item(New_PID)
    Push_Cart(Temp_Cart)

# 
# 
# 
# 
# 


def Push_Cart(Temp_Cart):
    SQL_Queries.Update_Field(CONSTANTS.USER_TABLE,)

def Pull_Cart(UID):
    Cart_List = SQL_Queries.Get_Cart(UID)
    return Cart_List.split(',')
    

def Add_Item(Cart, New_PID):
    Cart.append(New_PID)
    return Cart.sort()
