import threading

class KeyValueStore:
    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()

    def put(self, key, value):
        with self._lock:
            created = key not in self._data
            self._data[key] = value
            return created

    def get(self, key):
        with self._lock:
            return self._data.get(key)

    def delete(self, key):
        with self._lock:
            if key not in self._data:
                return False
            del self._data[key]
            return True