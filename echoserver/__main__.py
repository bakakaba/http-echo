from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler

from echohandler import EchoHandler


PORT = 8000


def run(server=ThreadingHTTPServer, handler=EchoHandler):
    try:
        server_address = ('', PORT)
        httpd = server(server_address, handler)
        print(f'Listening on port: {server_address[1]}')
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("\nTerminating")
        httpd.server_close()


run()
