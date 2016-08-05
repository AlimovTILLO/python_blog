import cgi, cgitb
import logging
from os import curdir
from os import environ
import settings
from dal import DataAccess
from template_engine.template import Template
from http.server import HTTPStatus
from git_template import template

def handle_index(request):
    user_id = is_authenticate(request)
    if user_id == -1:
        f = open(settings.TEMPLATES_DIR + 'index.html')
        read = f.read()
        html = template.Template(read).render(auth = False)
    else:
        f = open(settings.TEMPLATES_DIR + 'profile.html')
        read = f.read()
        data = get_userdata(request)
        posts = DataAccess.DataAccessor().select("select title, post from posts where user_id = '%s'" % user_id)
        html = template.Template(read).render(name = data[0][1], lname = data[0][2], username  = data[0][3], posts = posts)
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    # a = DataAccess.DataAccessor()
    # a.selectExample()
    return request

def post(request):
    user_id = is_authenticate(request)
    if  user_id == -1:
        f = open(settings.TEMPLATES_DIR + 'index.html')
        read = f.read()
        html = template.Template(read).render(auth = False)
    else:
        f = open(settings.TEMPLATES_DIR + 'profile.html')
        read = f.read()
        data = get_userdata(request)
        posts = DataAccess.DataAccessor().select("select * from posts where user_id = '%s'" % user_id)
        html = template.Template(read).render(name = data[0][1], lname = data[0][2], username  = data[0][3], posts = posts)
        data = return_value_from_post(request)
        DataAccess.DataAccessor().insert('posts', user_id = user_id, title = data['title'], post = data['text'] )
    redirect(request, '/')
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    # a = DataAccess.DataAccessor()
    # a.selectExample()
    return request


def login(request):
    if is_authenticate(request)==-1:
        f = open(settings.TEMPLATES_DIR + 'login.html')
        read = f.read()
        html = template.Template(read).render(msg = 'Enter login and password', auth = False)
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
        request.end_headers()
        request.wfile.write(str.encode(html))
    else:
        redirect(request,'/')
        request.end_headers()
    return request


def login_post(request):
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    a = return_value_from_post(request)
    f = open(settings.TEMPLATES_DIR + 'login.html')
    read = f.read()
    user_id = check_user(a['username'],a['password'])
    if user_id ==-1:
        html = template.Template(read).render(msg="The password you've ntered is incorrect", auth = False)
    else:
        html = template.Template(read).render(msg="Congrats yo logged in", auth = True)
        request.send_header('Set-Cookie', 'session=%s;path=/;' % authorize(a['username']))
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def register(request):
    context = {}
    html = Template('register.html', context).render()
    if is_authenticate(request) != -1:
        redirect(request, '/')
    else:
        request.send_response(HTTPStatus.OK)
        request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def reg_post(request):
    request.send_response(HTTPStatus.OK)
    values = return_value_from_post(request)
    a = DataAccess.DataAccessor()
    if a.is_exist_user(values['username']):
        txt = 'Already exist'
    else:
        a.insert(
            'users',
            name = values['name'],
            lname = values['lname'],
            username = str(values['username']).lower(),
            password = values['password'],
            active = True
        )
        session = generate_session()
        request.send_header('Set-Cookie', 'session=%s;path=/;' % session)
        a.insert(
            'sessions',
            id_user = str(get_id_by_username(values['username'])).lower(),
            session = session
        )
        txt = 'Created'
    context = {'status': txt}
    html = Template('registered.html', context).render()
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request

def logout(request):
    if is_authenticate(request)!=-1:
        cook = get_cookies(request)
        if "session" in cook:
            remove_session(cook['session'])
    request.send_response(HTTPStatus.TEMPORARY_REDIRECT)
    request.send_header('Set-Cookie', 'session=;path=/;')
    request.send_header('Location', 'http://localhost:8080/')
    request.end_headers()
    return request

def handle_404(request):
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request

def resetDB(request):
    a = DataAccess.DataAccessor()
    a.creteable()
    print("Data base updated")
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode('Data base updated'))
    return request

def return_value_from_post(request):
    logging.debug('POST %s' % (request.path))
    ctype, pdict = cgi.parse_header(request.headers['content-type'])
    if ctype == 'multipart/form-data':
        postvars = cgi.parse_multipart(request.rfile, pdict)
    elif ctype == 'application/x-www-form-urlencoded':
        length = int(request.headers['content-length'])
        postvars = cgi.parse_qs(request.rfile.read(length), keep_blank_values=1)
    else:
        postvars = {}
    logging.debug('TYPE %s' % (ctype))
    logging.debug('PATH %s' % (request.path))
    logging.debug('ARGS %d' % (len(postvars)))
    res = {}
    if len(postvars):
        i = 0
    for key in sorted(postvars):
        logging.debug('ARG[%d] %s=%s' % (i, key, postvars[key]))
        i += 1
        a = key.decode("utf-8")
        b = postvars[key][0].decode("utf-8")
        #print('ARG[%d] %s=%s' % (i, key, postvars[key]))
        res[a] = b
    return res

def generate_session():
    import random
    a = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    res = ''
    for i in range(90):
        res += random.choice(a)
    return res

def is_authenticate(request):
    cook = get_cookies(request)
    if 'session' in cook:
        a = DataAccess.DataAccessor()
        rows = a.select("select id_user from sessions where session='%s';" % cook['session'])
        if len(rows)!=0:
            return rows[0][0]
        else:
            return -1
    else:
        return -1

def get_cookies(request):
    res = {}
    cookie = (request.headers.get_all('Cookie', failobj={}))
    if len(cookie)>0:
        for i in cookie[0].split(';'):
            res[(i.strip().split('='))[0]]= i.strip().split('=')[1]
    return res

def get_id_by_username(username):
    #query = "select id from users order by id desc limit 1;"
    query = "select id from users where username='%s';"%username
    a = DataAccess.DataAccessor()
    rows = a.select(query)
    if len(rows) > 0:
        return rows[0][0]
    else:
        return -1

def check_user(username, password):
    """
    :param username:
    :param password:
    :return: user_id
    """
    a = DataAccess.DataAccessor()
    rows = a.select("select * from users where username='%s' and password='%s';" % (username, password))
    if len(rows)>0:
        return rows[0][0]
    else:
        return -1

def redirect(request, path):
    request.send_response(HTTPStatus.SEE_OTHER)
    request.send_header('Location', path)

def remove_session(session):
    a = DataAccess.DataAccessor()
    a.delete("sessions", session = session)

def authorize(username):
    a = DataAccess.DataAccessor()
    session = generate_session()
    a.insert("sessions", id_user = get_id_by_username(username), session = session)
    return session

def get_userdata(request):
    a = DataAccess.DataAccessor()
    return a.select("select * from users where id = '%s'" % is_authenticate(request))

