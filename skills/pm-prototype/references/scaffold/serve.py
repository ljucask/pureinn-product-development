#!/usr/bin/env python3
"""
Serve a prototype for the harness, and carry what a reviewer does back to the
project. Standard library only.

    python3 serve.py            # http://127.0.0.1:8931/...
    python3 serve.py 9000

WHAT IT SERVES. If this file sits in `build/` of a prototype folder (one with a
`meta.md` beside `build/`), the PROTOTYPE FOLDER is the root, so the harness can
reach `feature-cards/` and open at `/build/harness.html`. Otherwise it serves
its own folder and opens at `/harness.html`.

WHAT IT WRITES. Only into `review/` under the served root, and only these:

    review/notes/<time>-<who>.json   what a reviewer sent, complete
    review/notes.md                  the same, readable, appended
    review/proposals.json            edits proposed to a feature's description

A proposal is never applied here. The feature plan and the cards are the source
of truth for whoever builds from them; a browser does not get to rewrite them.
The author - or the agent working in the repo - reads `review/` and applies
what should be applied.

WHY IT IS SHAPED THIS WAY
- Bound to 127.0.0.1. It writes to disk; it is not for a network.
- Every write needs the `X-Harness: 1` header and a Host of this machine. A
  page on another site cannot send that header without a preflight this server
  does not answer, and a rebound DNS name does not carry this Host.
- No path ever comes from a request. File names are built here.
- Threaded, because a prototype may hold a connection open (a looping video)
  and a single-threaded server then blocks every other request.
- `Cache-Control: no-store`, so an edited config is picked up on reload.
"""
import json, os, re, sys, time, threading
from urllib.parse import unquote
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.dirname(HERE)
IS_PROTOTYPE = os.path.basename(HERE) == 'build' and os.path.isfile(os.path.join(PARENT, 'meta.md'))
ROOT = PARENT if IS_PROTOTYPE else HERE
PREFIX = 'build/' if IS_PROTOTYPE else ''
REVIEW = os.path.join(ROOT, 'review')
PORT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8931
MAX_BODY = 8 * 1024 * 1024          # notes may carry scaled screenshots
LOCK = threading.Lock()
ID_RE = re.compile(r'^[A-Za-z0-9_.-]{1,64}$')
SHELL = ('harness.html', 'harness.config.js', 'harness-client.js')
WATCH_EXT = ('.html', '.js', '.css', '.json', '.md', '.svg', '.png', '.jpg', '.jpeg', '.webp')


def slug(text, fallback='reviewer'):
    out = re.sub(r'[^a-z0-9]+', '-', str(text or '').lower()).strip('-')[:40]
    return out or fallback


_STAMP = {'at': 0.0, 'value': None}


def stamps():
    """Newest change among the shell files, and among everything else served.
    review/ is left out: saving a note must not look like the prototype changed.
    Held for a second: it walks the whole folder, and any page in the browser
    can request this URL in a loop."""
    now = time.time()
    if _STAMP['value'] is not None and now - _STAMP['at'] < 1.0:
        return _STAMP['value']
    _STAMP['at'] = now
    _STAMP['value'] = _walk_stamps()
    return _STAMP['value']


def _walk_stamps():
    shell = art = 0.0
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('review', 'node_modules')]
        for name in files:
            if name.startswith('.') or not name.lower().endswith(WATCH_EXT):
                continue
            try:
                m = os.path.getmtime(os.path.join(base, name))
            except OSError:
                continue
            if name in SHELL:
                shell = max(shell, m)
            else:
                art = max(art, m)
    return {'shell': shell, 'art': art}


def read_json(path, default):
    """A missing file is the default. A file that is there and cannot be read is
    an error, not an empty list - treating it as empty is how the next write
    replaces a history with one entry."""
    if not os.path.exists(path):
        return default
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def one_line(value, limit=80):
    """For anything that goes into notes.md beside the note text. The file is read
    by a person and by an agent; a field that carries a newline can write its
    own headings into it."""
    return re.sub(r'[`#\[\]]', '', re.sub(r'\s+', ' ', str(value or ''))).strip()[:limit]


def write_json(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def plain(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', str(html or ''))).strip()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=ROOT, **kw)

    def log_message(self, *a):
        pass

    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('X-Content-Type-Options', 'nosniff')
        super().end_headers()

    # ---- helpers
    def local_host(self):
        host = (self.headers.get('Host') or '').lower()
        return host in ('127.0.0.1:%d' % PORT, 'localhost:%d' % PORT)

    def reply(self, code, data):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(code)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def hidden(self):
        """Nothing whose path has a dot-segment is served: .git, .env, .DS_Store."""
        path = unquote(self.path.split('?', 1)[0].split('#', 1)[0]).replace('\\', '/')
        segs = [seg for seg in path.split('/') if seg]
        # review/ holds reviewers' names, notes and screenshots. The harness
        # reaches it through the endpoints; nothing needs it as a file.
        return any(seg.startswith('.') for seg in segs) or (bool(segs) and segs[0] == 'review')

    def translate_path(self, path):
        """A symlink inside the folder must not be a way out of it."""
        real = os.path.realpath(super().translate_path(path))
        root = os.path.realpath(ROOT)
        if real != root and not real.startswith(root + os.sep):
            return os.path.join(root, '.outside-the-served-folder')
        return real

    def cross_site(self):
        return (self.headers.get('Sec-Fetch-Site') or '') == 'cross-site'

    # ---- reads
    def do_GET(self):
        if not self.local_host():
            return self.reply(403, {'error': 'host'})
        route = self.path.split('?', 1)[0]
        if route.startswith('/__harness/') and self.cross_site():
            return self.reply(403, {'error': 'origin'})
        if route == '/__harness/ping':
            return self.reply(200, {'bridge': 1, 'prototype': IS_PROTOTYPE, 'prefix': PREFIX, 'writes': 'review/'})
        if route == '/__harness/changes':
            return self.reply(200, stamps())
        if route == '/__harness/proposals':
            try:
                return self.reply(200, read_json(os.path.join(REVIEW, 'proposals.json'), []))
            except (OSError, ValueError):
                return self.reply(500, {'error': 'review/proposals.json cannot be read'})
        if route.startswith('/__harness/'):
            return self.reply(404, {'error': 'unknown'})
        if self.hidden():
            return self.send_error(404)
        if route in ('/', ''):
            self.send_response(302)
            self.send_header('Location', '/' + PREFIX + 'harness.html')
            self.end_headers()
            return
        return super().do_GET()

    def do_HEAD(self):
        if not self.local_host() or self.hidden():
            return self.send_error(404)
        return super().do_HEAD()

    def list_directory(self, path):
        self.send_error(404)          # no directory listings
        return None

    # ---- writes
    def do_POST(self):
        if not self.local_host():
            return self.reply(403, {'error': 'host'})
        if self.headers.get('X-Harness') != '1':
            return self.reply(403, {'error': 'header'})
        if (self.headers.get('Content-Type') or '').split(';')[0].strip().lower() != 'application/json' or self.cross_site():
            return self.reply(415, {'error': 'type'})
        try:
            size = int(self.headers.get('Content-Length') or 0)
        except ValueError:
            size = -1
        if size <= 0 or size > MAX_BODY:
            return self.reply(413, {'error': 'size'})
        try:
            data = json.loads(self.rfile.read(size).decode('utf-8'))
        except (ValueError, UnicodeDecodeError):
            return self.reply(400, {'error': 'json'})
        if not isinstance(data, dict):
            return self.reply(400, {'error': 'shape'})
        route = self.path.split('?', 1)[0]
        if route == '/__harness/notes':
            return self.save_notes(data)
        if route == '/__harness/proposal':
            return self.save_proposal(data)
        return self.reply(404, {'error': 'unknown'})

    def save_notes(self, data):
        notes = data.get('notes')
        if not isinstance(notes, list):
            return self.reply(400, {'error': 'notes'})
        who = one_line(data.get('from'))
        at = time.strftime('%Y-%m-%dT%H-%M-%S')
        with LOCK:
            os.makedirs(os.path.join(REVIEW, 'notes'), exist_ok=True)
            # two saves in one second must not share a name: the second would
            # replace the first one's full record
            n = 0
            while True:
                name = '%s%s-%s.json' % (at, ('-%d' % n) if n else '', slug(who))
                if not os.path.exists(os.path.join(REVIEW, 'notes', name)):
                    break
                n += 1
            write_json(os.path.join(REVIEW, 'notes', name), data)
            lines = ['', '## %s - %s' % (at.replace('T', ' '), who or 'unnamed reviewer'), '']
            if data.get('asked'):
                lines += ['Asked: ' + plain(data['asked'])[:500], '']
            if data.get('overall'):
                lines += ['**Overall:** ' + plain(data['overall'])[:2000], '']
            for n in notes[:500]:
                if not isinstance(n, dict):
                    continue
                where = ' / '.join(one_line(n.get(k), 60) for k in ('screen', 'state', 'device') if n.get(k))
                view = ' / '.join(one_line(n.get(k), 40) for k in ('role', 'phase') if n.get(k) and n.get(k) != 'all')
                sev = str(n.get('severity') or 'normal')
                sev = sev if sev in ('low', 'normal', 'high') else 'normal'
                text = plain(n.get('html') or n.get('text'))[:2000] or '(a screenshot with no words)'
                lines.append('- [%s] %s%s%s - %s' % (
                    sev, where,
                    (' (' + view + ')') if view else '',
                    (' on `%s`' % re.sub(r'\s+', ' ', str(n.get('selector'))).replace('`', '').strip()[:120]) if n.get('selector') else '',
                    text))
            lines += ['', 'Full record: `review/notes/%s`' % name, '']
            md = os.path.join(REVIEW, 'notes.md')
            fresh = not os.path.exists(md)
            with open(md, 'a', encoding='utf-8') as fh:
                if fresh:
                    fh.write('# Review notes\n\nSaved from the harness. Newest at the bottom. '
                             'Each entry is routed by whoever works on the prototype - a note that flows nowhere is lost.\n')
                fh.write('\n'.join(lines))
        return self.reply(200, {'ok': 1, 'file': 'review/notes/' + name, 'count': len(notes)})

    def save_proposal(self, data):
        feature = str(data.get('feature') or '')
        field = str(data.get('field') or '')
        value = data.get('value')
        if not ID_RE.match(feature) or field not in ('desc', 'spec') or not isinstance(value, str):
            return self.reply(400, {'error': 'proposal'})
        entry = {
            'id': 'p%d' % int(time.time() * 1000),
            'at': time.strftime('%Y-%m-%dT%H:%M:%S'),
            'by': one_line(data.get('by')),
            'feature': feature, 'field': field,
            'was': str(data.get('was') or '')[:20000],
            'value': value[:20000],
            'status': 'open'
        }
        with LOCK:
            os.makedirs(REVIEW, exist_ok=True)
            path = os.path.join(REVIEW, 'proposals.json')
            try:
                items = read_json(path, [])
            except (OSError, ValueError):
                return self.reply(500, {'error': 'review/proposals.json cannot be read - fix or remove it'})
            if not isinstance(items, list):
                return self.reply(500, {'error': 'review/proposals.json is not a list'})
            # a newer proposal for the same field replaces an older open one
            for it in items:
                if isinstance(it, dict) and it.get('feature') == feature and it.get('field') == field and it.get('status') == 'open':
                    it['status'] = 'superseded'
            items.append(entry)
            write_json(path, items)
        return self.reply(200, {'ok': 1, 'proposal': entry})


if __name__ == '__main__':
    server = ThreadingHTTPServer(('127.0.0.1', PORT), Handler)
    server.daemon_threads = True
    # flushed: run in the background, stdout is a pipe, and the one line the
    # caller is waiting for would otherwise sit in a buffer
    print('Harness: http://127.0.0.1:%d/%sharness.html' % (PORT, PREFIX), flush=True)
    print('Serving: %s' % ROOT, flush=True)
    print('Review notes and proposed edits are saved to: %s' % REVIEW, flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
