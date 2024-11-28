from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Respond to HTTP GET requests
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Hello from %s!' % self.server.server_name.encode())
        print(f"Received GET request on {self.server.server_name}")

def run_server(server_name, port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.server_name = server_name
    print(f"{server_name} running on port {port}...")
    httpd.serve_forever()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python3 server.py <server_name> <port>")
        sys.exit(1)
    
    server_name = sys.argv[1]
    port = int(sys.argv[2])
    run_server(server_name, port)