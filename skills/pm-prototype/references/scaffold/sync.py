#!/usr/bin/env python3
"""
Keep the harness's feature list in step with the prototype's feature cards.
Standard library only. Run it from `build/`:

    python3 sync.py            # rewrite the generated block in harness.config.js
    python3 sync.py --check    # exit 1 if the config is out of date, change nothing
    python3 sync.py --apply    # first apply the open proposals in ../review/, then rewrite

WHY. The harness shows each feature's phase, user types and description. Those
are decided in the feature cards, and a second copy typed into the config by
hand is a second truth that drifts. So the config's `features` is generated,
between two markers, and nothing else in the config is touched.

WHAT IT READS. `../feature-cards/*.md` - the frontmatter of each card:

    id:      PRT-ORD-003          required
    title:   "Bulk assign"        the name shown in the harness
    state:   built | next | cut   a `cut` card is in no view; it is listed on
                                  the feature map with its `reason:`
    screen:  index.html           where it is, for "go to this feature" - only
                                  needed when it is marked inside the artifact
                                  and is not a whole screen
    phase:   mvp                  one of the phases declared in the config
    roles:   [dispatcher, admin]  who sees it; leave out for everyone
    summary: "One line."          the description; else the first paragraph
                                  under "## What it proves"
    versions: [A, B]              optional
    on:      {"index.html": ["#bulk"]}   optional, JSON, for an artifact that
                                         cannot carry data-feature

and, in the body, a `## Notes so far` section, which becomes the card's notes.

`phases`, `roles`, `versions` and `view` stay hand-written in the config. They
are asked once per project and rarely change; features change every session.

PROPOSALS. An edit made in the harness is saved by serve.py to
`../review/proposals.json` and changes nothing. `--apply` is the act of
accepting them: it writes each open proposal into its card (`summary:` for the
description, `## Notes so far` for the notes), marks it applied, and then
regenerates. Run it when the author has agreed to the edits, not before.
"""
import json, os, re, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.join(HERE, '..', 'feature-cards')
CONFIG = os.path.join(HERE, 'harness.config.js')
PROPOSALS = os.path.join(HERE, '..', 'review', 'proposals.json')
OPEN = '/* <generated:features> written by sync.py from ../feature-cards/ - change the cards, not this */'
CLOSE = '/* </generated:features> */'


def split_card(text):
    """(frontmatter lines, body) - or ([], text) when there is no frontmatter."""
    lines = text.lstrip('\ufeff').replace('\r', '').split('\n')
    if lines and lines[0].strip() == '---':
        for i in range(1, len(lines)):
            if lines[i].strip() == '---':
                return lines[1:i], '\n'.join(lines[i + 1:])
    return [], text


def scalar(raw):
    raw = raw.strip()
    if not raw:
        return ''
    if raw[0] in '{[' or raw[0] == '"':
        try:
            return json.loads(raw)
        except ValueError:
            pass
    if raw.startswith('[') and raw.endswith(']'):
        return [p.strip().strip('"\'') for p in raw[1:-1].split(',') if p.strip()]
    return raw.strip('"\'')


def frontmatter(lines, problems=None, who=''):
    """A small reader for the forms cards actually use: `key: value`, an inline
    list, inline JSON, a block list, and a folded or literal block. Anything it
    cannot read is REPORTED, never guessed - a `roles:` list that is silently
    dropped shows an admin-only feature to everyone."""
    out, i = {}, 0
    while i < len(lines):
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', lines[i])
        i += 1
        if not m:
            continue
        key, raw = m.group(1), m.group(2).rstrip()
        block = []
        while i < len(lines) and (lines[i].startswith((' ', '\t')) or not lines[i].strip()):
            if lines[i].strip():
                block.append(lines[i].strip())
            i += 1
        if raw in ('>', '>-', '>+'):
            out[key] = ' '.join(block)
        elif raw in ('|', '|-', '|+'):
            out[key] = '\n'.join(block)
        elif raw == '' and block and all(b.startswith('- ') or b == '-' for b in block):
            out[key] = [b[1:].strip().strip('"\'') for b in block if b[1:].strip()]
        elif block:
            if problems is not None:
                problems.append('%s: `%s:` continues over several lines in a form sync.py does not read - write it on one line' % (who, key))
            out[key] = scalar(raw)
        else:
            if raw and raw[0] not in '"\'[{':
                raw = re.sub(r'\s+#.*$', '', raw)        # a trailing comment is not part of the value
            value = scalar(raw)
            if key == 'on' and raw and not isinstance(value, (dict, list)):
                if problems is not None:
                    problems.append('%s: `on:` is not valid JSON and was ignored - use {"file.html": ["#selector"]}' % who)
                continue
            out[key] = value
    return out


def section(body, heading):
    """Text under `## heading`, up to the next `## `."""
    m = re.search(r'^##\s+' + re.escape(heading) + r'\s*$', body, re.M | re.I)
    if not m:
        return ''
    rest = body[m.end():]
    nxt = re.search(r'^##\s+', rest, re.M)
    return (rest[:nxt.start()] if nxt else rest).strip()


def first_paragraph(text):
    return re.sub(r'\s+', ' ', text.strip().split('\n\n')[0]).strip() if text.strip() else ''


def read_cards():
    feats, problems = [], []
    if not os.path.isdir(CARDS):
        return None, []
    for name in sorted(os.listdir(CARDS)):
        if not name.endswith('.md') or name.startswith('.'):
            continue
        with open(os.path.join(CARDS, name), encoding='utf-8') as fh:
            fm_lines, body = split_card(fh.read())
        fm = frontmatter(fm_lines, problems, name)
        fid = str(fm.get('id') or '')
        if not re.match(r'^[A-Za-z0-9_.-]{1,64}$', fid):
            problems.append('%s: no usable `id:` in the frontmatter - skipped' % name)
            continue
        state = str(fm.get('state') or fm.get('status') or 'built')
        if state == 'cut':
            # kept for the feature map only: a cut is a decision, and the reason
            # for it is the part worth keeping
            cut = {'id': fid, 'name': str(fm.get('title') or fid), 'status': 'cut'}
            reason = str(fm.get('reason') or '') or first_paragraph(section(body, 'Why it was cut'))
            if reason:
                cut['reason'] = reason
            feats.append(cut)
            continue
        f = {'id': fid, 'name': str(fm.get('title') or fid)}
        if fm.get('phase'):
            f['phase'] = str(fm['phase'])
        else:
            problems.append('%s: no phase yet' % fid)
        if state in ('built', 'next'):
            f['status'] = state
        desc = str(fm.get('summary') or '') or first_paragraph(section(body, 'What it proves'))
        if desc:
            f['desc'] = desc
        notes = section(body, 'Notes so far')
        if notes:
            f['spec'] = notes
        roles = fm.get('roles')
        if isinstance(roles, str) and roles:
            roles = [roles]
        if isinstance(roles, list) and roles:
            f['roles'] = [str(r) for r in roles]
        if isinstance(fm.get('versions'), list) and fm['versions']:
            f['versions'] = [str(v) for v in fm['versions']]
        if isinstance(fm.get('on'), (dict, list)) and fm['on']:
            f['on'] = fm['on']
        # where it is, for a feature marked only inside the artifact
        screen = fm.get('screen') or fm.get('built_in')
        if isinstance(screen, str):
            screen = [p.strip() for p in screen.split(',')]
        if isinstance(screen, list):
            screen = [str(p) for p in screen if str(p).lower().endswith(('.html', '.htm'))]
            if screen:
                f['screen'] = screen if len(screen) > 1 else screen[0]
        f['card'] = '../feature-cards/' + name
        feats.append(f)
    return feats, problems


def render(feats):
    body = json.dumps(feats, ensure_ascii=False, indent=2).replace('\n', '\n  ')
    # The block sits between two comment markers in a JS file. Text from a card
    # - or from a proposal someone typed into the harness - must not be able to
    # write a marker of its own: `*/` would end the block early and leave the
    # rest of it behind as live code. Inside a JS string `\/` is just `/`.
    body = body.replace('*/', '*\\/').replace('</', '<\\/')
    return '%s\n  features: %s,\n  %s' % (OPEN, body, CLOSE)


def rewrite(config, block):
    if config.count(OPEN) > 1 or config.count(CLOSE) > 1:
        return None                     # two blocks is a file somebody should look at
    a, b = config.find(OPEN), config.find(CLOSE)
    if a > -1 and b > a:
        return config[:a] + block + config[b + len(CLOSE):]
    # first run on a config that only has the plain line
    m = re.search(r'^([ \t]*)features:\s*\[\s*\],[ \t]*$', config, re.M)
    if m:
        return config[:m.start()] + m.group(1) + block + config[m.end():]
    return None


def set_summary(fm_lines, value):
    line = 'summary: ' + json.dumps(value, ensure_ascii=False)
    for i, ln in enumerate(fm_lines):
        if re.match(r'^summary:\s*', ln):
            # a folded or literal summary runs on over indented lines; they go
            # with the key, or they are left behind as orphans under the new one
            j = i + 1
            while j < len(fm_lines) and (fm_lines[j].startswith((' ', '\t')) or not fm_lines[j].strip()):
                j += 1
            return fm_lines[:i] + [line] + fm_lines[j:]
    return fm_lines + [line]


def set_notes(body, value):
    m = re.search(r'^##\s+Notes so far\s*$', body, re.M | re.I)
    if not m:
        return body.rstrip('\n') + '\n\n## Notes so far\n\n' + value.strip() + '\n'
    rest = body[m.end():]
    nxt = re.search(r'^##\s+', rest, re.M)
    tail = rest[nxt.start():] if nxt else ''
    return body[:m.end()] + '\n\n' + value.strip() + '\n' + ('\n' + tail if tail else '')


def apply_proposals():
    try:
        with open(PROPOSALS, encoding='utf-8') as fh:
            items = json.load(fh)
    except (OSError, ValueError):
        print('no proposals to apply')
        return 0
    done = 0
    for it in items:
        if not isinstance(it, dict) or it.get('status') != 'open':
            continue
        fid = str(it.get('feature') or '')
        if not re.match(r'^[A-Za-z0-9_.-]{1,64}$', fid):
            continue
        path = None
        for name in sorted(os.listdir(CARDS)) if os.path.isdir(CARDS) else []:
            if not name.endswith('.md'):
                continue
            with open(os.path.join(CARDS, name), encoding='utf-8') as fh:
                fm_lines, _ = split_card(fh.read())
            if str(frontmatter(fm_lines).get('id') or '') == fid:
                path = os.path.join(CARDS, name)
                break
        if not path:
            print('  skipped %s: no card with that id' % fid)
            continue
        with open(path, encoding='utf-8', newline='') as fh:
            original = fh.read()
        eol = '\r\n' if '\r\n' in original else '\n'
        bom = '\ufeff' if original.startswith('\ufeff') else ''
        fm_lines, body = split_card(original)
        value = str(it.get('value') or '')
        if it.get('field') == 'desc':
            fm_lines = set_summary(fm_lines, value)
        elif it.get('field') == 'spec':
            body = set_notes(body, value)
        else:
            continue
        with open(path, 'w', encoding='utf-8', newline='') as fh:
            fh.write(bom + ('---\n' + '\n'.join(fm_lines) + '\n---\n' + body).replace('\n', eol))
        it['status'] = 'applied'
        it['applied_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')
        done += 1
        print('  applied %s (%s)' % (fid, it.get('field')))
    # serve.py may have taken a new proposal while this ran: read the file
    # again, carry over only what was applied here, and replace it in one move
    applied = {it.get('id'): it for it in items if isinstance(it, dict) and it.get('status') == 'applied' and it.get('applied_at')}
    try:
        with open(PROPOSALS, encoding='utf-8') as fh:
            latest = json.load(fh)
    except (OSError, ValueError):
        latest = items
    for i, it in enumerate(latest):
        if isinstance(it, dict) and it.get('id') in applied and it.get('status') == 'open':
            latest[i] = applied[it['id']]
    tmp = PROPOSALS + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(latest, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, PROPOSALS)
    return done


def main():
    args = sys.argv[1:]
    if '--apply' in args:
        print('applied %d proposal(s)' % apply_proposals())
    feats, problems = read_cards()
    if feats is None:
        # Wrap mode, or a prototype with no cards yet: the feature list in the
        # config is written by hand, and it is not this script's to replace
        print('no ../feature-cards/ folder - nothing to generate, harness.config.js left as it is')
        return 0
    try:
        with open(CONFIG, encoding='utf-8') as fh:
            config = fh.read()
    except OSError:
        print('no harness.config.js beside sync.py')
        return 2
    new = rewrite(config, render(feats))
    if new is None:
        print('harness.config.js needs exactly one generated block, or a plain `features: [],` line - fix it and run again')
        return 2
    for p in problems:
        print('  note: ' + p)
    if '--check' in args:
        if new != config:
            print('harness.config.js is out of date - run sync.py')
            return 1
        print('up to date: %d feature(s)' % len(feats))
        return 0
    if new != config:
        with open(CONFIG, 'w', encoding='utf-8') as fh:
            fh.write(new)
        print('wrote %d feature(s) into harness.config.js' % len(feats))
    else:
        print('up to date: %d feature(s)' % len(feats))
    return 0


if __name__ == '__main__':
    sys.exit(main())
