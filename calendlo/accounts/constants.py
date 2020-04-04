ACCOUNT_ROLES = [
    ('EDU', 'EDUCATION'),
    ('MED', 'MEDICAL'),
    ('MUS', 'MUSIC'),
    ('DNC', 'DANCE'),
    ('OTH', 'OTHERS'),
]

import re

USER_IDENTIFIER_REGEX = re.compile("^\w+$")
