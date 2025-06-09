from http.server import HTTPServer, SimpleHTTPRequestHandler
import webbrowser
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# HTTP server to serve index.html
def run_http_server(port=8000):
    try:
        server_address = ('', port)
        httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
        logger.info(f"Starting HTTP server on port {port}")
        url = f"http://localhost:{port}"
        logger.info(f"Opening {url} in your default browser...")
        webbrowser.open(url)
        httpd.serve_forever()
    except OSError as e:
        logger.error(f"Failed to start HTTP server on port {port}: {e}")
        raise

if __name__ == "__main__":
    try:
        run_http_server()
    except Exception as e:
        logger.error(f"Server failed: {e}")