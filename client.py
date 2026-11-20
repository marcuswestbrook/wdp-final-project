import http.client
import json
from urllib.parse import quote

class NodeClient:
    def __init__(self, host, port, timeout=2.0):
        self.host, self.port, self.timeout = host, port, timeout

    def request(self, method, key, value=None):
        path = "/" + quote(key, safe="")
        body = None if value is None else value.encode("utf-8")
        connection = http.client.HTTPConnection(
            self.host, self.port, timeout=self.timeout
        )
        try:
            connection.request(method, path, body=body)
            response = connection.getresponse()
            raw = response.read()
            return response.status, json.loads(raw) if raw else None
        finally:
            connection.close()