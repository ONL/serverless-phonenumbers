from http.server import BaseHTTPRequestHandler
import phonenumbers

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        length = int(self.headers.getheader('content-length'))
        field_data = self.rfile.read(length)
        #fields = urlparse.parse_qs(field_data)
        
        #if fields["N"] is not None:
        #    param_num = fields["N"]
        #else:
        #    param_num = "+12345678"
        
        #if fields["C"] is not None:
        #    param_country = fields["C"]
        #else:
        #    param_country = None
        param_num = "+12345678"
        param_country = None
        num = phonenumbers.parse(param_num, param_country)
        message = str(phonenumbers.is_valid_number(num))
        message = str(field_data)
        self.wfile.write(message.encode())
        return
