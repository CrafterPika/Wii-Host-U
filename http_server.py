from http.server import HTTPServer, BaseHTTPRequestHandler

ip_adress = input("Please enter your IP address: ")

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/www/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

print("Server is running at port 8080")
httpd = HTTPServer((ip_adress, 8080), Serv)
httpd.serve_forever()