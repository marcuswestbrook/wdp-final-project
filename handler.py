from http.server import BaseHTTPRequestHandler

class KVHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        key = self.read_key_or_error()
        if key is None:
            return
        value = self.read_body_or_error()
        if value is None:
            return
        created = self.server.store.put(key, value)
        self.send_json(201 if created else 200, {"key": key})

    def do_GET(self):
        key = self.read_key_or_error()
        if key is None:
            return
        value = self.server.store.get(key)
        if value is None:
            self.send_json(404, {"error": "key not found"})
        else:
            self.send_json(200, {"key": key, "value": value})

    def do_DELETE(self):
        key = self.read_key_or_error()
        if key is None:
            return
        if self.server.store.delete(key):
            self.send_response(204)
            self.end_headers()
        else:
            self.send_json(404, {"error": "key not found"})