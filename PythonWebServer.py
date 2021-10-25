
from http.server import BaseHTTPRequestHandler, HTTPServer
import re
import os
import subprocess
import socket

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if None != re.search('/api/setBrightness/*', self.path):
            param = self.path.split('/')[-1]
            if param:
                num = float(param)
            else:
                num = 1
            print()
            ##print (self.path.split('/'))
           
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()

            if num < 1:
                num = 1
            elif num > 100:
                num = 100
             
            script = "powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1," + str(num) + ")"

            subprocess.Popen(script, shell=True)
                        
            message = "Impostata luminosita schermo " + str(num)
            self.wfile.write(bytes(message, "utf8")) 
            return
        
                    

def run():
    print('Avvio del server...')
 
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    port = 8081
    
    server_address = (IPAddress, port)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('Server in esecuzione su ' + str(IPAddress) + ":" + str(port))
    httpd.serve_forever()
    
run()
