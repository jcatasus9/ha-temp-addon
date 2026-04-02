from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        cpu = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1000
        nvme = int(open('/sys/class/hwmon/hwmon1/temp1_input').read()) / 1000

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(f'{"cpu": {cpu}, "nvme": {nvme}}'.encode())

HTTPServer(("0.0.0.0", 5001), Handler).serve_forever()
