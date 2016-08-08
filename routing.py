from exceptions import RouteNotFoundException
from method_handlers import handle_404
import settings
import os
ROUTE_NOT_FOUND_EXCEPTION_MESSAGE = 'Route for method {method} and path {path} not found'


class Router(object):
    def __init__(self):
        self.routes = []


    def handle(self, request):
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



class Route(object):
    def __init__(self, method, path, handler_func):
        self._method = method
        self._path = str(path).lower()
        self._handler = handler_func

    def get_handler(self):
        return self._handler
    
    def check_method_and_path(self, method, path):
        return (self._method == method and self._path == path.split('?')[0]) or (os.path.isfile(settings.STATIC_DIR + path) and self._path=='/static')
