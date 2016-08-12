# # # a = 'asSD234'
# # # print(a.lower())
# #
# # # import cookielib
# # # import urllib2
# # #
# # # cookies = cookielib.LWPCookieJar()
# # # handlers = [
# # #     urllib2.HTTPHandler(),
# # #     urllib2.HTTPSHandler(),
# # #     urllib2.HTTPCookieProcessor(cookies)
# # #     ]
# # # opener = urllib2.build_opener(*handlers)
# # #
# # # def fetch(uri):
# # #     req = urllib2.Request(uri)
# # #     return opener.open(req)
# # #
# # # def dump():
# # #     for cookie in cookies:
# # #         print cookie.name, cookie.value
# # #
# # # uri = 'http://facebook.com/'
# # # res = fetch(uri)
# # # dump()
# # #
# # # res = fetch(uri)
# # # dump()
# # #
# # # # save cookies to disk. you can load them with cookies.load() as well.
# # # cookies.save('mycookies.txt')
# # #
# # #
# # #
# # #
# #
# #
# # # import requests
# # #
# # # url = "http://localhost:8080/"
# # # url = 'https://www.facebook.com/'
# # # r = requests.get(url,timeout=5)
# # # if r.status_code == 200:
# # #     for cookie in r.cookies:
# # #         print(cookie)
# #
# # !/usr/bin/python
# # -*- coding: utf-8 -*-
#
# #
# # {% each post_id %}
# #             <h2>{{ it }}</h2>
# #
# #         {% end %}
#
#
# #title=posts[i][1], text=posts[i][2]
# # {% each id %}{{ it }}{% end %}
#
#
#
# import psycopg2
# import psycopg2.extras
# import sys
#
# import settings
#
# con = None
# user_id = 2
# uid = 2
# try:
#
#     con = psycopg2.connect(
#         database=settings.DATABASES['postgreSQL']['name'],
#         user=settings.DATABASES['postgreSQL']['user'],
#         password=settings.DATABASES['postgreSQL']['password'],
#         host=settings.DATABASES['postgreSQL']['host']
#     )
#
#     cursor = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
#     cursor.execute("SELECT * FROM posts WHERE user_id=%(user_id)s", {'user_id': user_id})
#
#     rows = cursor.fetchall()
#
#     for row in rows:
#         print("%s" % (row["id"]))
#         cursor.execute("SELECT * FROM posts WHERE Id=%(id)s", {'id': row["id"]})
#         # print(cursor.fetchone())
#
#
#
# except psycopg2.DatabaseError as e:
#     print('Error %s' % e)
#     sys.exit(1)
#
#
# finally:
#
#     if con:
#         con.close()
# #
# # #
# # import re
# #
# # embed_url = '/post/123'
# # response = re.findall(r'\d+', embed_url)
# # # re.search(r'^(http://)?(localhost:8081\.)?(post)?(\d+)', embed_url)
# # try:
# #     k = int(response[0])
# #
# # except IndexError:
# #     k = None
# #
# # print(k)
# def posts(request):
#     user_id = is_authenticate(request)
#     if user_id == -1:
#         f = open(settings.TEMPLATES_DIR + 'index.html')
#         read = f.read()
#         html = template.Template(read).render(auth=False)
#     else:
#         f = open(settings.TEMPLATES_DIR + 'profile.html')
#         read = f.read()
#         data = get_userdata(request)
#         posts = DataAccess.DataAccessor().select("select * from posts where user_id = '%s'" % user_id)
#         html = template.Template(read).render(name=data[0][1], lname=data[0][2], username=data[0][3], posts=posts)
#
#         data = return_value_from_post(request)
#         DataAccess.DataAccessor().insert('posts', user_id=user_id, title=data['title'], post=data['text'])
#
#     redirect(request, '/')
#     request.send_header('Content-Type', 'text/html')
#     request.end_headers()
#     request.wfile.write(str.encode(html))
#     # a = DataAccess.DataAccessor()
#     # a.selectExample()
#
#     return request