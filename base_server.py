from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import os

class ExampleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        rootdir = "./htdocs/"
        try:
            if self.path.endswith('.html'):
                print 'Finding...'
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404, 'file not present')
    
    def do_POST( self ):
        rootdir = "./htdocs/"
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)
                self.send_response(200)
                self.send_header('Content-type','text-html')
                self.end_headers()
                self.wfile.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404, 'file not present')
            
def run():
    print('Example base server is starting.')
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, ExampleHTTPRequestHandler)
    print('Example base server is running.....')
    httpd.serve_forever()
    
if __name__=='__main__':
    run()