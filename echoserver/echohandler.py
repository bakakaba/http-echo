from functools import partial
from http import HTTPStatus
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
            self.close_connection = True
            return
        if not self.parse_request():
            return
        self.send_response(200)
        self.end_headers()

        self.wfile
        self.wfile.write(bytes(str(self.headers), 'utf-8'))

        remaining = int(self.headers.get('content-length'))
        while True:
            if remaining <= 0:
                break

            buf = BUFFER_SIZE if remaining > BUFFER_SIZE else remaining
            self.wfile.write(self.rfile.read(buf))
            remaining -= buf

        self.wfile.flush()
