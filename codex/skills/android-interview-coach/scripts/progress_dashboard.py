#!/usr/bin/env python3
"""Render a stable local progress dashboard and serve it on localhost."""
import argparse
import json
import socket
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def render(template_path: Path, data_path: Path) -> str:
    template = template_path.read_text(encoding="utf-8")
    data = json.loads(data_path.read_text(encoding="utf-8"))
    return template.replace("__PROGRESS_DATA__", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))


def free_port(start: int) -> int:
    for port in range(start, start + 50):
        with socket.socket() as sock:
            try:
                sock.bind(("127.0.0.1", port))
                return port
            except OSError:
                continue
    raise RuntimeError("No free localhost port found")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path.home() / ".codex/android-interview-coach/progress.json")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    html = render(root / "assets/dashboard.html", args.data)

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path not in ("/", "/index.html"):
                self.send_error(404)
                return
            body = html.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, fmt, *args):
            pass

    port = free_port(args.port)
    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    print(f"http://127.0.0.1:{port}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
