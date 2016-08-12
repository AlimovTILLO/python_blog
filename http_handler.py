import cgi
import logging
from http.server import BaseHTTPRequestHandler

from routes import routes
from routing import Router


class Handler(BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        self.router = Router()
        self.router.register_routes(routes)
        super().__init__(request, client_address, server)

    def do_GET(self):
        self.router.handle(request=self)
        return

    def do_POST(self):
        self.router.handle(request=self)
        return

    def do_PUT(self):
        self.router.handle(request=self)
        return

    def do_PATCH(self):
        self.router.handle(request=self)
        return

    def do_DELETE(self):
        self.router.handle(request=self)
        return

    def do_OPTIONS(self):
        self.router.handle(request=self)
        return

    def do_HEAD(self):
        self.router.handle(request=self)
        return
