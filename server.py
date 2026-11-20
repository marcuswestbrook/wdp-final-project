import argparse
from http.server import ThreadingHTTPServer
from handler import KVHandler
from store import KeyValueStore

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()
    with ThreadingHTTPServer(("127.0.0.1", args.port), KVHandler) as server:
        server.store = KeyValueStore()
        server.serve_forever()

if __name__ == "__main__":
    main()