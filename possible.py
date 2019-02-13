from http.server import BaseHTTPRequestHandler
import phonenumbers
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        if "?" in self.path:
            params = dict(urllib.parse.parse_qsl(self.path.split("?")[1], True))
            param_num = params.get("N","+1")
            param_country = params.get("C")
                 
        if param_country == "xx":
            param_country = None
        
        num = phonenumbers.parse(param_num, param_country)
        message = str(phonenumbers.is_possible_number(num))
        
        self.wfile.write(message.encode())
        return
    
    def do_POST(self):
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        if self.rfile:
            # print urlparse.parse_qs(self.rfile.read(int(self.headers['Content-Length'])))
            params = dict(urllib.parse.parse_qs(self.rfile.read(int(self.headers['Content-Length']))))
            param_num = params["N"]
            param_country = params["C"]
        
        num = phonenumbers.parse(param_num, param_country)
        message = str(phonenumbers.is_possible_number(num))
        
        self.wfile.write(message.encode())
        return
