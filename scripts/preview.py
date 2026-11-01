"""Serve a built Pages project at its real subpath, only on localhost."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        parsed = urlsplit(path)
        if parsed.path.startswith("/vecord-support/"):
            path = parsed.path[len("/vecord-support"):]
        return super().translate_path(path)

    def do_GET(self):
        path = urlsplit(self.path)
        if not path.path.startswith("/vecord-support/"):
            self.send_error(404)
            return
        super().do_GET()

    def do_HEAD(self):
        if not urlsplit(self.path).path.startswith("/vecord-support/"):
            self.send_error(404)
            return
        super().do_HEAD()

    def send_error(self, code, message=None, explain=None):
        page = Path(self.directory) / "404.html"
        if code != 404 or not page.exists():
            super().send_error(code, message, explain)
            return
        data = page.read_bytes()
        self.send_response(404)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(data)


if __name__ == "__main__":
    cli = argparse.ArgumentParser()
    cli.add_argument("--directory", required=True)
    cli.add_argument("--port", type=int, default=8027)
    args = cli.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=args.directory))
    print(f"Preview: http://127.0.0.1:{args.port}/vecord-support/", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
