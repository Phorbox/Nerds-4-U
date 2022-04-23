# session id -> UID
# UID -> Shopping Cart lsit(as a string)
# convert string to list of Pid
# get Select pids
# paste pids into cart
import SQL_Queries,CONSTANTS


def Add_To_Cart(UID,PID):
    Cart = Pull_Cart(UID)
    Cart = Add_Item(Cart,PID)
    Push_Cart(Cart,UID)

def Push_Cart(Temp_Cart,UID):

    SQL_Queries.Update_Field(CONSTANTS.USER_TABLE,"Cart",Temp_Cart,"UID",UID)

def Pull_Cart(UID):
    Cart_List = SQL_Queries.Get_Cart(UID)
    Cart_List = Cart_List[1:-1]
    Cart_List = Cart_List.split(',')
    Cart_List = Str_To_Lint(Cart_List)
    
    return Cart_List

def Add_Item(Cart, New_PID):
    PID_Set = set(Cart)
    if New_PID not in PID_Set:
        PID_Set.add(New_PID)
        Cart.insert(0,New_PID)
    Cart.sort()
    return Cart

def Add_Item(Cart, New_PID):
    PID_Set = set(Cart)
    if New_PID not in PID_Set:
        PID_Set.add(New_PID)
        Cart.insert(0,New_PID)
    Cart.sort()
    return Cart

def Str_To_Lint(String_List):
    for i in range(0, len(String_List)):
        String_List[i] = int(String_List[i])
    return String_List

def Delete_From_Cart(UID,PID):
    print("test")
    Cart = Pull_Cart(UID)
    Cart.remove(PID)
    Push_Cart(Cart,UID)

Delete_From_Cart(130,1)