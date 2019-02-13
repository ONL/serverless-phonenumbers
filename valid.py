from http.server import BaseHTTPRequestHandler
import phonenumbers

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        
        length = int(self.headers.getheader('content-length'))
        field_data = self.rfile.read(length)
        print field_data
        fields = urlparse.parse_qs(field_data)
        print(*fields, sep = ", ")
        
        if fields["N"] is not None:
            param_num = fields["N"]
        else:
            param_num = "+12345678"
        
        if fields["C"] is not None:
            param_country = fields["C"]
        else:
            param_country = None
        
        num = phonenumbers.parse(param_num, param_country)
        message = str(phonenumbers.is_valid_number(num))
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write(message.encode())
        return
