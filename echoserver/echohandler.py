from functools import partial
from http import HTTPStatus
from sys import stdout
from http.server import BaseHTTPRequestHandler

BUFFER_SIZE = 1024 * 64


class EchoHandler(BaseHTTPRequestHandler):

    def handle_one_request(self):
        """Modified request handler

        Overridden to generically handle any HTTP requests
        """

        self.raw_requestline = self.rfile.readline(BUFFER_SIZE + 1)
        if len(self.raw_requestline) > BUFFER_SIZE:
            self.requestline = ''
            self.request_version = ''
            self.command = ''
            self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
            return
        if not self.raw_requestline:
            return
        if not self.parse_request():
            return

        response = self.raw_requestline
        response += bytes(str(self.headers), 'utf-8')
        try:
            length = int(self.headers.get('content-length') or 0)

            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(response) + length)
            self.end_headers()

            self.wfile.write(response)
            if length:
                remaining = length
                while True:
                    if remaining <= 0:
                        break

                    buf = BUFFER_SIZE if remaining > BUFFER_SIZE else remaining
                    self.wfile.write(self.rfile.read(buf))
                    remaining -= buf

            self.wfile.flush()
        except BrokenPipeError:
            print('Connection terminated before send completed.')
        finally:
            stdout.flush()
