a = 'asSD234'
print(a.lower())

# import cookielib
# import urllib2
#
# cookies = cookielib.LWPCookieJar()
# handlers = [
#     urllib2.HTTPHandler(),
#     urllib2.HTTPSHandler(),
#     urllib2.HTTPCookieProcessor(cookies)
#     ]
# opener = urllib2.build_opener(*handlers)
#
# def fetch(uri):
#     req = urllib2.Request(uri)
#     return opener.open(req)
#
# def dump():
#     for cookie in cookies:
#         print cookie.name, cookie.value
#
# uri = 'http://facebook.com/'
# res = fetch(uri)
# dump()
#
# res = fetch(uri)
# dump()
#
# # save cookies to disk. you can load them with cookies.load() as well.
# cookies.save('mycookies.txt')
#
#
#
#


# import requests
#
# url = "http://localhost:8080/"
# url = 'https://www.facebook.com/'
# r = requests.get(url,timeout=5)
# if r.status_code == 200:
#     for cookie in r.cookies:
#         print(cookie)