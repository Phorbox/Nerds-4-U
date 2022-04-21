# session id -> UID
# UID -> Shopping Cart lsit(as a string)
# convert string to list of Pid
# get Select pids
# paste pids into cart


def Add_To_Cart(UID,New_PID):
    Temp_Cart = Pull_Cart(UID)
    Temp_Cart = Add_Item(New_PID)
    Push_Cart(Temp_Cart)

def Push_Cart(Temp_Cart):
    pass

def Pull_Cart(Temp_Cart):
    pass

def Add_Item(Temp_Cart):
    pass