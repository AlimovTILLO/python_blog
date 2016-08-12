import os

HOSTNAME = 'localhost'
PORT = 8080

TEMPLATES_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'templates/')
STATIC_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static')

DATABASES = {
    'postgreSQL': {
        'name': 'test1',
        'host': 'localhost',
        'user': 'adminaka',
        'password': '123'
    }
}
