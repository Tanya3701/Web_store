from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """Класс, который отвечает за обработку входящих запросов от клиентов"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("../templates/contacts.html", "r", encoding="utf-8") as f:
            self.wfile.write(bytes(f.read(), "utf-8"))

    def do_POST(self):
        """Метод для обработки входящих Post-запросов"""
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data)
        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    httpd = HTTPServer((hostName, serverPort), MyServer)
    print("server started at %s:%s" % (hostName, serverPort))

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("server stopped")
