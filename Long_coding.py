from datetime import datetime

class UserData:
    users = []
    def __init__(self, user_id:int, user_name:str, mail_id:str, phone_no:str, password:str):
        #constructor for initializing user data
        self.user_id = user_id
        self.user_name = user_name
        self.mail_id = mail_id
        self.phone_no = phone_no
        self.password = password

#user Functionality
class UserFunctionality:
    def validate_user(self, mail_id, password=None):
        registered_mail_id = [user.mail_-id for user in UserData.users if user.mail_id == mail_id]

        if not registered_mail_id and password == None:
            return True
        else:
            varified_password  = [user]