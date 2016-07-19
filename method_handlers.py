from template_engine.template import Template
from http.server import HTTPStatus


def handle_index(request):
    context = {'content': 'Hello world'}

    html = Template('index.tpl', context).render()
    request.send_response(HTTPStatus.OK)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    request.wfile.write(str.encode(html))
    return request


def handle_404(request):
    request.send_response(HTTPStatus.NOT_FOUND)
    request.send_header('Content-Type', 'text/html')
    request.end_headers()
    return request
