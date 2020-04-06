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

ERR_INVALID_TIME_DURATION = {
    "msg": "can not book for more than 1 hour",
    "error_code": "APP_0001"
}

ERR_INVALID_TIME_INTERVAL = {
    "msg": "invalid timings",
    "error_code": "APP_0002"
}

ERR_USER_NOT_AVAILABLE = {
    "msg": "User not free for given timings",
    "error_code": "APP_0003"
}

INVALID_QUERY_PARAMS = "Invalid query params"

SUCCESSFUL_APPOINTMENT = {
    "msg": "Appointment created Successfully!!"
}

##### availability app #####
