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

sys.exit(fail)
