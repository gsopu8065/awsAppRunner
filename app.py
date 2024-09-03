from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('Hello, World!')

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()

    # Run the WSGI server
    server = make_server('0.0.0.0', 8000, app)
    print("Serving on http://0.0.0.0:8000")
    server.serve_forever()
