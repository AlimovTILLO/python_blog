from exceptions import RouteNotFoundException
from method_handlers import handle_404
import settings
ROUTE_NOT_FOUND_EXCEPTION_MESSAGE = 'Route for method {method} and path {path} not found'
import re

class Router(object):
    def __init__(self):
        self.routes = []
    #
    # def check_static(self, path):
    #     if path.endswith(".css") or path.endswith(".jpg"):
    #         return True
    #     else:
    #         return False


    def handle(self, request):
        # if self.check_static( request.path):
        #     self.send_static(request, request.path)
        # else:
        try:
            handler = self._get_handler_for_path(request.command, request.path)
            handler(request)
        except RouteNotFoundException:
            handle_404(request)

    def register_route(self, route):
        self.routes.append(route)

    def register_routes(self, routes):
        if type(routes) != list:
            raise TypeError("Routes must be list")
        self.routes.extend(routes)

    def _get_handler_for_path(self, method, path):
        for route in self.routes:
            if route.check_method_and_path(method, path):
                return route.get_handler()
        raise RouteNotFoundException(ROUTE_NOT_FOUND_EXCEPTION_MESSAGE.format(method=method, path=path))

    # def send_static(self, request, path):
    #     print('%%%%%%%% path =',settings.STATIC_DIR + request.path )
    #     try:
    #         sendReply = False
    #         if path.endswith(".html"):
    #             mimetype = 'text/html'
    #             sendReply = True
    #         if path.endswith(".jpg"):
    #             mimetype = 'image/jpg'
    #             sendReply = True
    #         if path.endswith(".gif"):
    #             mimetype = 'image/gif'
    #             sendReply = True
    #         if path.endswith(".png"):
    #             mimetype = 'image/png'
    #             sendReply = True
    #         if path.endswith(".js"):
    #             mimetype = 'application/javascript'
    #             sendReply = True
    #         if path.endswith(".css"):
    #             mimetype = 'text/css'
    #             sendReply = True
    #             f = open(settings.STATIC_DIR + request.path)
    #
    #         if sendReply:
    #             # Open the static file requested and send it
    #             request.send_response(200)
    #             request.send_header('Content-type', mimetype)
    #             f = open(settings.STATIC_DIR + request.path)
    #             # if path.endswith(".jpg"):
    #             #     read = self.load_binary(request.path)
    #             #     request.end_headers()
    #             #     request.wfile.write(bytes(read, 'utf-8'))
    #             # else:
    #             #     read = f.read()
    #             #     request.end_headers()
    #             #     request.wfile.write(bytes(read, 'utf-8'))
    #             request.wfile.write(f.read())
    #             f.close()
    #             return
    #     except IOError:
    #         request.send_error(404, 'File Not Found: %s' % request.path)
    #
    # def load_binary(self, file):
    #     with open(file, 'rb') as file:
    #         return file.read()


class Route(object):
    def __init__(self, method, path, handler_func):
        self._method = method
        self._path = path
        self._handler = handler_func

    def get_handler(self):
        return self._handler
    
    def check_method_and_path(self, method, path):
        if re.match(self._path, path) and self._method == method:
                return True
        return False

        #return self._method == method and self._path == path.split('?')[0]

