from http.server import BaseHTTPRequestHandler
import phonenumbers
import urllib.parse

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        if "?" in self.path:
            params = dict(urllib.parse.parse_qsl(self.path.split("?")[1], True, True))
            param_num = params.get("N", "+12345678")
            param_country = params.get("C")
            param_type = params.get("T")
        
        #if param_country == "None": param_country = None
        num = phonenumbers.parse(param_num, param_country)
        
        if param_type == "INT":
            message = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
        elif param_type == "NAT":
            message = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.NATIONAL)
        else:
            message = phonenumbers.format_number(num, phonenumbers.PhoneNumberFormat.E164)
        
        self.wfile.write(message.encode())
        return
