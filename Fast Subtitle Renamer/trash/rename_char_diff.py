import os

def getchars(string):
    chars = {}
    for char in string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def getchardiff(chars1, chars2):
    chardiff = 0
    for char in chars1:
        if char in chars2:
            chardiff += abs(chars2[char] - chars1[char])
            del chars2[char]
        else:
            chardiff += chars1[char]
    for char in chars2:
        chardiff += chars2[char]
    return chardiff

videxts = ['.webm', '.flv', '.ogg', '.ogv', '.drc', '.mng', '.avi', '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg', '.mpeg', '.mp2', '.mpe', '.mpv', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.mkv']
subexts = ['.srt', '.smi', '.ssa', '.sub', '.sbv']

dirlist = os.listdir()

subs = []
vids = []
for d in dirlist:
    name, ext = os.path.splitext(d)
    if ext in videxts:
        vids.append(d)
    elif ext in subexts:
        subs.append(d)

for sub in subs:
    subchars = getchars(os.path.splitext(sub)[0])
    mindiff = 100000 #!
    mindiffvid = None
    for vid in vids:
        vidchars = getchars(os.path.splitext(vid)[0])
        chardiff = getchardiff(subchars, vidchars)
        if chardiff < mindiff:
            mindiff = chardiff
            mindiffvid = vid
    os.rename(sub, os.path.splitext(mindiffvid)[0] + os.path.splitext(sub)[1])
