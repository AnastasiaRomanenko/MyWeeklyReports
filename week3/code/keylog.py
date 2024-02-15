from http.server import BaseHTTPRequestHandler, HTTPServer

class SendHelloWorld(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello World!")
        else:
            self.send_error(404, 'Endpoint not found')

port=7886
server_address = ('', port)
httpd = HTTPServer(server_address, SendHelloWorld)
print(f'Starting HTTP server on port {port}...')
httpd.serve_forever()


