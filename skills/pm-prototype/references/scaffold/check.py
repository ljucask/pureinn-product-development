#!/usr/bin/env python3
"""
Structural checks for harness.html, runnable before any change ships.

The first one exists because the same defect was introduced four times in one
sitting and is invisible to `node --check`: the file is one very long IIFE whose
setup code runs more than a thousand lines above its helpers, so a
module-level `var` read by a function that setup calls is `undefined` at that
moment. Sometimes it throws and takes the whole boot with it; sometimes
`undefined` is falsy and it silently behaves - which is worse.

The rule this enforces: anything an init-time function reads is either declared
above the first call, or lives inside the function.

    python3 check.py            # exits non-zero on a finding
"""
import re, sys, os

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'harness.html')
src = re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', open(path).read(), re.S)[0]
lines = src.split('\n')
fail = 0

decl = {}
for i, ln in enumerate(lines):
    m = re.match(r'^  var ([A-Za-z_$][\w$]*)\s*=', ln)
    if m: decl.setdefault(m.group(1), i)

fns = {}
for i, ln in enumerate(lines):
    m = re.match(r'^  function ([A-Za-z_$][\w$]*)\s*\(', ln)
    if m:
        j = i + 1
        while j < len(lines) and not re.match(r'^  \}', lines[j]): j += 1
        fns[m.group(1)] = (i, j)

calls = []
for i, ln in enumerate(lines):
    m = re.match(r'^  ([A-Za-z_$][\w$]*)\s*\(\s*\)\s*;\s*$', ln)
    if m and m.group(1) in fns: calls.append((m.group(1), i))

bad = []
for fname, cline in calls:
    a, b = fns[fname]
    body = '\n'.join(lines[a:b])
    for vname, vline in decl.items():
        if vline > cline and re.search(r'(?<![\w$.])' + re.escape(vname) + r'(?![\w$])', body):
            bad.append((fname, cline + 1, vname, vline + 1))

print("use-before-assignment  %d module functions, %d init-time calls" % (len(fns), len(calls)))
for f, c, v, d in bad:
    print("  FAIL %s() called line %d reads `%s`, declared line %d" % (f, c, v, d))
    fail = 1
if not bad: print("  ok")

# no <body> state class may share a name with an element class - the collision
# that blanked the whole page twice before the is- prefix rule existed
states = set(re.findall(r'body\.(is-[a-z-]+)', open(path).read()))
elems  = set(re.findall(r'^\s*\.([a-z][\w-]*)\s*[,{]', open(path).read(), re.M))
clash  = states & elems
print("state/element name clash")
if clash:
    for c in sorted(clash): print("  FAIL body state `%s` is also an element class" % c)
    fail = 1
else: print("  ok")

# Functions called but never defined. `node --check` passes on these because it
# is a parse check, not a resolve check, and the browser only notices when the
# path is taken - which is how press() survived a commit after an edit replaced
# it instead of adding beside it, silently killing the note, mark and share
# menus while the state and mockup menus carried on working.
BUILTINS = set("""
if for while switch catch function return typeof new delete void do else try
Object Array String Number Boolean Math JSON Date RegExp Promise Error Set Map
parseInt parseFloat isNaN setTimeout setInterval clearTimeout clearInterval
requestAnimationFrame cancelAnimationFrame encodeURIComponent decodeURIComponent
encodeURI decodeURI fetch alert confirm prompt matchMedia getComputedStyle
createImageBitmap structuredClone queueMicrotask btoa atob eval
""".split())

defined = set(fns) | set(decl)
defined |= set(re.findall(r'(?:var|let|const)\s+([A-Za-z_$][\w$]*)\s*=\s*function', src))
defined |= set(re.findall(r'function\s+([A-Za-z_$][\w$]*)\s*\(', src))
defined |= set(re.findall(r'(?:var|let|const)\s+([A-Za-z_$][\w$]*)', src))
defined |= set(re.findall(r'function[^(]*\(([^)]*)\)', src) and
               [a.strip() for g in re.findall(r'function[^(]*\(([^)]*)\)', src)
                for a in g.split(',') if a.strip()])

# Strip strings and comments with a real scanner, not a regex. The file builds
# CSS inside JS strings, and a regex that pairs quotes gets one apostrophe out
# of step and then exposes every string after it - which produced a page of
# false findings about calc(), var() and rgba().
def strip_literals(t):
    out, i, n = [], 0, len(t)
    while i < n:
        c = t[i]
        if c == '/' and i + 1 < n and t[i+1] == '*':
            k = t.find('*/', i + 2); i = n if k < 0 else k + 2; out.append(' ')
        elif c == '/' and i + 1 < n and t[i+1] == '/':
            k = t.find('\n', i); i = n if k < 0 else k; out.append(' ')
        elif c in '\'"`':
            q, i = c, i + 1
            while i < n and t[i] != q:
                i += 2 if t[i] == '\\' else 1
            i += 1; out.append('""')
        else:
            out.append(c); i += 1
    return ''.join(out)

code = strip_literals(src)

called = set()
for m in re.finditer(r'(?<![\w$.])([A-Za-z_$][\w$]*)\s*\(', code):
    called.add(m.group(1))

missing = sorted(n for n in called - defined - BUILTINS if not n[0].isupper())
print("called but never defined")
if missing:
    for n in missing: print("  FAIL %s() is called and has no definition" % n)
    fail = 1
else: print("  ok")

sys.exit(fail)
