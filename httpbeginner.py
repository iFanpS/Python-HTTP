from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        
        output = ('<body><html>')
        output += ('<h1>Hi Everyone This Is Me iFanpS</h1>')
        output += ('<h3>Here the link to my Social Media</h3>')
        output += ('<a href="https://github.com/iFanpS">This my Github</a>')
        output += ('</body></html>')

        self.wfile.write(output.encode())

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), helloHandler)
    print("server running on port %s" % PORT)
    server.serve_forever()

if __name__ == '__main__':
	main()