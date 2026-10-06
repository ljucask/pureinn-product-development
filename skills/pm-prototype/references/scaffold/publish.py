#!/usr/bin/env python3
"""Prepare a prototype for publishing as a Claude artifact.

    python3 publish.py                         # bundle the folder this file is in
    python3 publish.py --release r3 --title "Round 3" --note "New queue header" --note "Bulk assign added"
    python3 publish.py --out ../publish

A published prototype is one page plus the files beside it. The harness is the
page; the screens, the client script and the feature cards are the files. This
script does the four things that otherwise go wrong by hand:

  1. The page is the harness WITHOUT its document skeleton (the host supplies
     one), with harness.config.js written into it - a page that fetches its
     own config can be shown before the config arrives.
  2. `index.html` is the host's own name for the page, so a screen called
     index.html is renamed and every reference to it is rewritten.
  3. The store's access rules are generated from the config's `access` block,
     so what the harness offers a person and what the store accepts from them
     are the same thing, said once.
  4. Nothing that is not the prototype goes out: `review/` (people's notes),
     the bridge, this script, dot-files.

It writes a folder and prints what to hand to the Artifact tool. It publishes
nothing itself: publishing sends the prototype outside the machine, and that is
the author's decision each time.
"""
import argparse
import json
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# Never part of a published prototype.
SKIP_FILES = {'harness.html', 'harness.config.js', 'serve.py', 'sync.py', 'check.py', 'publish.py',
              'pull.py', 'README.md', 'HISTORY.md'}
SKIP_DIRS = {'review', 'publish', 'node_modules', '__pycache__'}
TEXT = {'.html', '.htm', '.js', '.css', '.md', '.json', '.svg', '.txt'}
RENAMED = 'home.html'

LEVELS = {'contributor': 'interact', 'editor': 'admin', 'owner': 'owner'}


def fail(msg):
    sys.stderr.write('publish: ' + msg + '\n')
    sys.exit(1)


def read(path):
    with open(path, encoding='utf-8', newline='') as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(text)


def access_of(config):
    """The `access` block, read without running the config. Unknown values fall
    back to the defaults - the same defaults the harness applies."""
    out = {'versions': 'editor', 'allNotes': 'owner'}
    m = re.search(r'\baccess\s*:\s*\{([^}]*)\}', config)
    if m:
        for key, allowed in (('versions', ('contributor', 'editor')), ('allNotes', ('editor', 'owner'))):
            v = re.search(r'\b' + key + r'''\s*:\s*['"](\w+)['"]''', m.group(1))
            if v and v.group(1) in allowed:
                out[key] = v.group(1)
    return out


def rules_for(access):
    """Each person writes under their own id. Everyone reads every version (a
    proposal is for the room); only whoever `allNotes` names reads other
    people's notes; only the author writes what belongs to somebody else,
    which is what approving a version is."""
    return [
        {'path': 'notes', 'read': LEVELS[access['allNotes']], 'write': 'owner'},
        {'path': 'notes/{self}', 'read': 'interact', 'write': 'interact'},
        {'path': 'versions', 'read': 'view', 'write': 'owner'},
        {'path': 'versions/{self}', 'read': 'view', 'write': LEVELS[access['versions']]},
    ]


def page_from(harness, config, release):
    # The real tags, found by where they sit. The stylesheet's own comments
    # mention <body>, and the script writes whole documents as strings, so the
    # first "<body>" in the file is not the body.
    style = re.search(r'<style>(.*?)</style>\s*</head>', harness, re.S)
    body = re.search(r'</head>\s*<body>(.*)</body>\s*</html>\s*$', harness, re.S)
    title = re.search(r'<title>(.*?)</title>', harness, re.S)
    if not (style and body):
        fail('harness.html does not look like the harness (no <style> or <body>).')
    name = re.search(r'''\btitle\s*:\s*(['"])(.*?)\1''', config)
    label = name.group(2) if name else (title.group(1) if title else 'Prototype')
    tag = '<script src="harness.config.js"></script>'
    if body.group(1).count(tag) != 1:
        fail('expected exactly one harness.config.js script tag in harness.html.')
    inline = config.replace('</script', '<\\/script')
    if release:
        inline += '\n;(window.HARNESS_CONFIG = window.HARNESS_CONFIG || {}).release = ' + \
            json.dumps(release, ensure_ascii=False).replace('</', '<\\/') + ';\n'
    inner = body.group(1).replace(tag, '<script>\n' + inline + '\n</script>')
    safe = label.replace('&', '&amp;').replace('<', '&lt;')
    return '<title>' + safe + '</title>\n<style>' + style.group(1) + '</style>\n' + inner


def main():
    ap = argparse.ArgumentParser(description='Bundle a prototype for publishing as a Claude artifact.')
    ap.add_argument('--src', default=HERE, help='the prototype build folder (default: where this file is)')
    ap.add_argument('--out', default=None, help='where to write the bundle (default: ../publish)')
    ap.add_argument('--release', default=None, help='an id for this release; people see its notes once')
    ap.add_argument('--title', default='New in this version')
    ap.add_argument('--note', action='append', default=[], help='one line of what changed; repeatable')
    a = ap.parse_args()

    src = os.path.abspath(a.src)
    out = os.path.abspath(a.out or os.path.join(src, '..', 'publish'))
    if out == src or src.startswith(out + os.sep):
        fail('the bundle cannot be written over the prototype itself.')
    for need in ('harness.html', 'harness.config.js'):
        if not os.path.isfile(os.path.join(src, need)):
            fail(need + ' not found in ' + src)
    if a.note and not a.release:
        fail('--note needs --release: a release note is shown once per release id.')

    files = []
    for root, dirs, names in os.walk(src):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')
                         and not os.path.islink(os.path.join(root, d))
                         and os.path.abspath(os.path.join(root, d)) != out)
        for n in sorted(names):
            full = os.path.join(root, n)
            rel = os.path.relpath(full, src).replace(os.sep, '/')
            if n.startswith('.') or os.path.islink(full) or (root == src and n in SKIP_FILES):
                continue
            files.append(rel)

    rename = 'index.html' in files
    if rename and RENAMED in files:
        fail('both index.html and ' + RENAMED + ' exist; rename one before publishing.')
    # index.html, when it is a whole path segment's file name and not part of a longer name
    ref = re.compile(r'(?<![\w.-])index\.html(?![\w-])')

    def fix(text):
        return ref.sub(RENAMED, text) if rename else text

    if os.path.isdir(out):
        shutil.rmtree(out)
    os.makedirs(out)

    config = read(os.path.join(src, 'harness.config.js'))
    access = access_of(config)
    release = {'id': a.release, 'title': a.title, 'notes': a.note} if a.release else None
    page = page_from(read(os.path.join(src, 'harness.html')), fix(config), release)
    write(os.path.join(out, 'prototype.html'), page)

    published, rewritten = {}, []
    for rel in files:
        target = RENAMED if rel == 'index.html' else rel
        dest = os.path.join(out, 'files', target)
        if os.path.splitext(rel)[1].lower() in TEXT:
            try:
                text = read(os.path.join(src, rel))
            except UnicodeDecodeError:
                text = None
            if text is not None:
                new = fix(text)
                if new != text:
                    rewritten.append(rel)
                write(dest, new)
                published[target] = 'files/' + target
                continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.copyfile(os.path.join(src, rel), dest)
        published[target] = 'files/' + target

    caps = {'db': {'rules': rules_for(access)}, 'user': {'scopes': ['profile']}, 'sample': {}}
    write(os.path.join(out, 'capabilities.json'), json.dumps(caps, indent=2) + '\n')
    write(os.path.join(out, 'files.json'), json.dumps(published, indent=2) + '\n')

    size = len(page.encode('utf-8'))
    print('Bundle written to ' + out)
    print('  page          prototype.html (' + str(size // 1024) + ' KB)')
    print('  files         ' + str(len(published)) + ' beside it (files.json maps published path -> source)')
    if rename:
        print('  renamed       index.html -> ' + RENAMED + '; references rewritten in: ' +
              (', '.join(['harness.config.js'] + rewritten)))
    print('  access        notes: any Contributor · versions: ' + access['versions'].capitalize() +
          ' · everyone\'s notes: ' + access['allNotes'].capitalize() + ' · approving: the author')
    print('  release       ' + (a.release + ' (' + str(len(a.note)) + ' notes)' if a.release else 'none'))
    print('  left out      review/, the bridge and the scripts')
    print()
    print('Publish with the Artifact tool: file_path = prototype.html, root = this folder,')
    print('files = files.json, capabilities = capabilities.json. To update a published')
    print('prototype pass its url as well; the notes and versions people left stay.')


if __name__ == '__main__':
    main()
