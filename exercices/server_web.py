from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(type(environ))
    print(environ)
    start_response('200 OK', [])
    return [b'<h1>coucou</h1>', b'<p>cmoi</p>']


server = make_server('0.0.0.0', 8000, application)
print('Serving on http://0.0.0.0:8000')
server.serve_forever()
