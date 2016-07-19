from http.server import HTTPServer
from http_handler import Handler

import settings

ADDRESS = (settings.HOSTNAME, settings.PORT)

server = HTTPServer(ADDRESS, Handler)

print("Started at {0}:{1}".format(*ADDRESS))


def main():
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()

if __name__ == '__main__':
    main()
