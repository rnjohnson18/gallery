#!/usr/bin/env python3

import time
import os
import sys

try:
    # Sets the output directory for index.html, defaulting to the current folder
    outdir = sys.argv[1]
except IndexError:
    outdir = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(outdir, 'index.html')

f = open(output, 'w')

def write(text):
    f.write(text)
    print(text)

# Double braces to escape the {} needed by CSS
write("""
<!DOCTYPE HTML>
<html>
<head>
<title>The OpenGLolol Gallery!</title>
<style>
body {{
    font-family: sans-serif;
}}

img {{
    border: 2px solid black;
}}
</style>
</head>

<body>
<h1>Introducing, the OpenGLolol Gallery! <span style="font-size:75%">(featuring Microsoft Paint and the <a href="https://ircnet.overdrivenetworks.com/">OVERdrive Community</a>)</span></h1>
<p>This page was automatically generated on <em>{}</em> by a script <a href="{}">(source)</a></p>
<p>Some images have captions for more context if you hover over them. :)</p>

""".format(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()), os.path.basename(__file__)))

files = os.listdir(outdir)
for file in files:
    # Iterate over .jpeg, .jpg, .png, and .gif files
    fileext = os.path.splitext(file)
    if fileext[1].lower() in ('.jpg', '.jpeg', '.png', '.gif', '.svg'):
        try:  # If a .txt file with the same name exists, use that as caption
            with open(fileext[0] + '.txt') as descfile:
                data = descfile.read()
                if data:  # But only if the .txt file isn't empty...
                    desc = "%s [%s]" % (data, file)
                else:
                    desc = file
        except OSError:  # Otherwise, fall back to just the file name as caption
            desc = file
        desc = "%s - Last modified %s" % (desc, time.ctime(os.path.getmtime(file)))
        write('<img src="%s" title="%s">\n' % (file, desc))

write("""</body>
</html>""")
f.close()