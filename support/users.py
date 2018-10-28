# This file stores user information that are used in tests

users = [
    {'name': 'valid company',
     'company name': 'Made Up Company',
     'email': 'muc@gmail.com',
     'address': 'Minties gatve, Vilnius Vilniaus apskritis, Lithuania',
     'website': 'http://MUC.com',
     'phone': '+37060511111',
     'info': 'From internet'
     },
    # Some items for this user are empty. This user is used for tests that check empty mandatory fields
    {'name': 'invalid company',
     'company name': ' ',
     'email': ' ',
     'address': 'Vilnius, Lithuania',
     'website': 'http://MUC.com',
     'phone': '+37060511111',
     },
]


def get_user(name):
    try:
        return (user for user in users if user['name'] == name).next()
    except TypeError:
        print '\n     User %s is not defined, enter a valid user.\n' % name
