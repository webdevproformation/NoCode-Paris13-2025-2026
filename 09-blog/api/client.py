from baserowapi import Baserow, Filter
from dotenv import dotenv_values

config = dotenv_values(".env")

def init():
    baserow = Baserow(token=config.get("TOKEN_BASE_ROW"))
    return baserow.get_table(config.get("ID_TABLE_USER"))



def find_user_by( column : str  , email : str ):
    # SELECT * FROM users WHERE email = email
    # https://www.jimwitte.net/baserowapi/client.html

    table = init()

    where = Filter(column, email)

    result = table.get_rows(filters=[where] , include=[ "email", "password" , "pseudo"])

    if len(result) == 1 :
        return result[0].to_dict()
    
    return None

    
def add_user( new_user ):
    table = init()

    table.add_rows(new_user)    