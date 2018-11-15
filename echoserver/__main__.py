from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from echohandler import EchoHandler


PORT = 8000


def run(server=ThreadingHTTPServer, handler=EchoHandler):
    server_address = ('', PORT)
    httpd = server(server_address, handler)
    print(f'Serving on http://localhost:{server_address[1]}')
    httpd.serve_forever()


run()
