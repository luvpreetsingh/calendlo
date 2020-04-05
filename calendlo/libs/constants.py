##### accounts app #####

ACCOUNT_ROLES = [
    ('EDU', 'EDUCATION'),
    ('MED', 'MEDICAL'),
    ('MUS', 'MUSIC'),
    ('DNC', 'DANCE'),
    ('OTH', 'OTHERS'),
]

import re

USER_IDENTIFIER_REGEX = re.compile("^\w+$")

SUCCESSFUL_SIGNUP = {
    "msg": "Successfully Signed Up!!"
}

ERR_USER_DOES_NOT_EXIST = {
    "msg": "User does not exist for given identifier",
    "error_code": "ACC_0001"
}

ERR_INVALID_PASSWORD = {
    "msg": "Password is incorrect",
    "error_code": "ACC_0002"
}


##### appointments app #####