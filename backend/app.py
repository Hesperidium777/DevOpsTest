#!/usr/bin/env python3
"""
Простой HTTP-сервер на Python, который отвечает на запросы.
"""

import http.server
import socketserver
import logging
import os
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

PORT = 8080
HOST = '0.0.0.0'

class HealthHandler(http.server.SimpleHTTPRequestHandler):
    """Обработчик HTTP-запросов с healthcheck."""
    
    def do_GET(self):
        """Обработка GET-запросов."""
        if self.path == '/health':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
            logger.info(f"Health check from {self.client_address[0]}")
            return
        
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('X-Backend-Server', 'python-http-server')
            self.send_header('X-Backend-Version', '1.0')
            self.end_headers()
            
            response = "Hello from Hesperidium!"
            self.wfile.write(response.encode('utf-8'))
            
            logger.info(f"Served request from {self.client_address[0]}: {self.path}")
            return
        
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Not Found')
        logger.warning(f"404 Not Found: {self.path} from {self.client_address[0]}")
    
    def log_message(self, format, *args):
        """Кастомное логирование сообщений."""
        logger.info(f"{self.address_string()} - {format % args}")

def run_server():
    """Запуск HTTP-сервера."""
    handler = HealthHandler
    
    with socketserver.TCPServer((HOST, PORT), handler) as httpd:
        server_info = httpd.socket.getsockname()
        logger.info(f"Server started on {server_info[0]}:{server_info[1]}")
        logger.info(f"Process ID: {os.getpid()}")
        logger.info(f"Current time: {datetime.now().isoformat()}")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            logger.info("Server stopped by user")
        finally:
            httpd.server_close()
            logger.info("Server closed")

if __name__ == "__main__":

    run_server()
