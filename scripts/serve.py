#!/usr/bin/env python3
"""Serve the portable app on this computer. Python 3.8+; no packages to install."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse
import sys
import webbrowser

ROOT = Path(__file__).resolve().parents[1]

class LocalHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

def create_server(port=8765):
    dist = ROOT / 'dist'
    if not (dist / 'index.html').is_file():
        raise RuntimeError('dist/ is missing. Run: python3 scripts/build.py')
    return ThreadingHTTPServer(('127.0.0.1', port), partial(LocalHandler, directory=str(dist)))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765, help='Local port (default: 8765)')
    parser.add_argument('--open', action='store_true', help='Open the app in your default browser')
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error('--port must be between 1 and 65535')
    try:
        server = create_server(args.port)
    except OSError as error:
        print(f'Could not start the local server: {error}', file=sys.stderr)
        print('If that port is busy, try: python3 scripts/serve.py --port 8766 --open', file=sys.stderr)
        return 1
    except RuntimeError as error:
        print(error, file=sys.stderr)
        return 1
    url = f'http://127.0.0.1:{args.port}/'
    print(f'Self-Mastery Field Guide: {url}', flush=True)
    print('Keep this terminal open. Press Control-C to stop. Internet is not required.', flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
    finally:
        server.server_close()
    return 0

if __name__ == '__main__':
    sys.exit(main())
