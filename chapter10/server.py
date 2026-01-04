#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # index.html を返す
        if self.path == "/" or self.path == "/index.html" or self.path == "/ws_index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()

            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "Not Found")

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')

        print("=== 受信データ ===")
        print(data)
        print("=================")

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == "__main__":
    server = HTTPServer(("", 80), MyHandler)
    print("HTTP Server running on port 80...")
    server.serve_forever()