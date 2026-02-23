import requests 

from baserowapi import Baserow, Filter

def find_user_by_email( email ):
    # SELECT * FROM users WHERE email = email

    # https://www.jimwitte.net/baserowapi/client.html

    table = baserow.get_table(849395)

    where = Filter("email", email)

    result = table.get_rows(filters=[where])

    return result

    