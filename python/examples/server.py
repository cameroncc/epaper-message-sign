#!/usr/bin/env python3

import socket
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from shakkeel_examples import clean_up_display_resources, display_message


class MeetingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        print(f"the path is {path}")

        if path == "/in_meeting":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Call your display_message function in a separate thread
            threading.Thread(
                target=display_message, args=("In a meeting",), daemon=True
            ).start()

            self.wfile.write(
                b"<html><body><h1>In Meeting</h1><p>Meeting status updated</p></body></html>"
            )

        elif path in ("/not_in_meeting", "/free"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Call your display_message function in a separate thread
            threading.Thread(
                target=display_message, args=("Free",), daemon=True
            ).start()

            self.wfile.write(
                b"<html><body><h1>Not In Meeting</h1><p>Meeting status updated</p></body></html>"
            )

        elif path == "/ip":
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("192.168.27.1", 53))
            ip = s.getsockname()[0]
            s.close()

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Call your display_message function in a separate thread
            threading.Thread(target=display_message, args=(ip,), daemon=True).start()

            self.wfile.write(
                b"<html><body><h1>Displaying IP address</h1></body></html>"
            )

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"<html><body><h1>404 Not Found</h1></body></html>")


def run_server(port=8000):
    server_address = ("", port)
    httpd = HTTPServer(server_address, MeetingHandler)
    print(f"Starting server on port {port}")
    print(f"Access endpoints at:")
    print(f"  http://localhost:{port}/in_meeting")
    print(f"  http://localhost:{port}/not_in_meeting")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.shutdown()
        clean_up_display_resources()


if __name__ == "__main__":
    run_server()
