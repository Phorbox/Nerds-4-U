class user:
  def __init__ (self,User_Name,UID,First_Name,Last_Name,Email,review_score,Phone_No):
    self.User_Name=User_Name
    self.UID=UID
    self.First_Name=First_Name
    self.Last_Name=Last_Name
    self.Email=Email

    self.review_score=review_score

    self.Phone_No=Phone_No
    

    def To_MySQL(self):
      return [self.user_name, self.UID, self.first_name, self.last_name, self.Email, self.review_Score, self.Phone_No]

    def New_MYSQL(self):
      return [self.user_name, self.first_name, self.last_name, self.Email, 0, self.Phone_No]
