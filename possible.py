from http.server import BaseHTTPRequestHandler
import phonenumbers

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        if (None == param_num) {
          param_num = "+12345678"
        }
        
        if (None == param_country) {
          param_country = None
        }
        
        num = phonenumbers.parse(param_num, param_country)
        message = phonenumbers.is_possible_number(num)
        self.wfile.write(message.encode())
        return
