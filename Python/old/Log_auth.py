Default_User = 'admin'
Default_Pass = 'admin'

class Auth_Key:
  def __init__ (self,User_Name):
    temp = Auth_SQL_Ping(User_Name)

    self.User_Name= temp[0]
    self.Pass = temp[1]
    self.UID = temp[2]


    def Auth_SQL_Ping(I_Name):
        sql = "SELECT %s FROM users"
        return (Default_User,Default_Pass,3)