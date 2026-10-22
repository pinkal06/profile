#!/usr/bin/env python3
"""
Pinkal Rathod – Personal Portfolio Static Web Server
A lightweight, zero-dependency Python server for local development and preview.
Runs using Python standard library without requiring Django or SQLite database queries.
"""

import http.server
import socketserver
import os
import sys
import webbrowser

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class PortfolioHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable caching headers and modern security policy
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

def run_server():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    
    with socketserver.TCPServer(("127.0.0.1", PORT), PortfolioHTTPRequestHandler) as httpd:
        url = f"http://127.0.0.1:{PORT}/"
        print("=" * 60)
        print("  PINKAL RATHOD – PERSONAL PORTFOLIO (STATIC WEB SERVER)")
        print("=" * 60)
        print(f"  Local URL    : {url}")
        print(f"  Serving Dir  : {DIRECTORY}")
        print("  Backend State: Decoupled (Zero Django/DB queries needed)")
        print("  Press Ctrl+C to stop the server.")
        print("=" * 60)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer gracefully stopped.")

if __name__ == '__main__':
    run_server()
