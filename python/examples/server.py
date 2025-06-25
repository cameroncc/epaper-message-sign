#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

from shakkeel_examples import display_message


class MeetingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path

        if path == "/in_meeting":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Call your display_message function here
            display_message("In a meeting")

            self.wfile.write(
                b"<html><body><h1>In Meeting</h1><p>Meeting status updated</p></body></html>"
            )

        elif path == "/not_in_meeting":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()

            # Call your display_message function here
            display_message("Free")

            self.wfile.write(
                b"<html><body><h1>Not In Meeting</h1><p>Meeting status updated</p></body></html>"
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


if __name__ == "__main__":
    run_server()
