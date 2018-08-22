import pyperclip

pyperclip.copy("Heyo")
text = pyperclip.paste()
print text

# Without dependencies

import subprocess

ENCODING = 'utf-8'

def _stringifyText(text):
    if not isinstance(text, (str, int, float, bool)):
        raise PyperclipException('only str, int, float, and bool values can be copied to the clipboard, not %s' % (text.__class__.__name__))
    return str(text)

def pbcopy(text):
    text = _stringifyText(text) # Converts non-str values to str.
    p = subprocess.Popen(['pbcopy', 'w'],
                            stdin=subprocess.PIPE, close_fds=True)
    p.communicate(input=text.encode(ENCODING))

def pbpaste():
    p = subprocess.Popen(['pbpaste', 'r'],
                            stdout=subprocess.PIPE, close_fds=True)
    stdout, stderr = p.communicate()
    return stdout.decode(ENCODING)


pbcopy("hellooo")
print pbpaste()
