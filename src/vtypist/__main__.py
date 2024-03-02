import subprocess

dom = "win2k22"
srcfile = "keys"
src=None

#KEY_LEFTCTRL KEY_ESC

# translation table
tt = {}

tt['\n'] = 'KEY_ENTER'
tt['.'] = 'KEY_DOT'
tt[':'] = 'KEY_LEFTSHIFT KEY_DOT'
tt['/'] = 'KEY_LEFTSHIFT KEY_7'
tt['}'] = 'KEY_RIGHTALT KEY_0'
tt['-'] = 'KEY_SLASH'
tt['\\'] = 'KEY_RIGHTALT KEY_MINUS'
tt[' '] = 'KEY_SPACE'
tt['ß'] = 'KEY_MINUS'
tt['"'] = 'KEY_LEFTSHIFT KEY_2'
tt['?'] = 'KEY_LEFTSHIFT KEY_MINUS'
tt['ä'] = 'KEY_APOSTROPHE'
tt['Ä'] = 'KEY_LEFTSHIFT KEY_APOSTROPHE'
tt['ö'] = 'KEY_SEMICOLON'
tt['Ö'] = 'KEY_LEFTSHIFT KEY_SEMICOLON'
tt[';'] = 'KEY_LEFTSHIFT KEY_COMMA'
tt['='] = 'KEY_LEFTSHIFT KEY_0'

for c in '0123456789':
    tt[c] = 'KEY_%s' % c

for c in 'abcdefghijklmnopqrstuvwxyz':
    tt[c] = 'KEY_%s' % c.upper()

for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    tt[c] = 'KEY_LEFTSHIFT KEY_%s' % c.upper()

tt['y'] = 'KEY_Z'
tt['Y'] = 'KEY_LEFTSHIFT KEY_Z'

with open(srcfile, 'r') as f:
    src = f.read().replace("\r", "")

for c in src:
    if c in tt:
        cmd = """virsh send-key %s %s""" % (dom, tt[c])
        print(cmd)
        subprocess.call(cmd, shell=True)
