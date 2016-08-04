from routing import Route
from constants import HTTP_METHODS
import method_handlers

routes = [
    Route(HTTP_METHODS.GET, '/', method_handlers.handle_index),
    Route(HTTP_METHODS.GET, '/resetdb/', method_handlers.resetDB),
    Route(HTTP_METHODS.GET, '/register/', method_handlers.register),
    Route(HTTP_METHODS.POST, '/register/', method_handlers.reg_post),
    Route(HTTP_METHODS.GET, '/logout/', method_handlers.logout),
    Route(HTTP_METHODS.GET, '/login/', method_handlers.login),
    Route(HTTP_METHODS.POST, '/login/', method_handlers.login_post)
]