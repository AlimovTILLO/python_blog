import os

HOSTNAME = 'localhost'
PORT = 8080

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates')


DATABASES = {
    'postgreSQL': {
        'name':'blog',
        'host': 'localhost',
        'user': 'bloguser',
        'password': '123'
    }
}










