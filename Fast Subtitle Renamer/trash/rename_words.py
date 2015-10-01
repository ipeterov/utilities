import os, re

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

def getuniques(namelist):
    words = []
    for name in namelist:
        words.append(set(re.split('\W+', name)))

    wordrate = {}
    for name in words:
        for word in name:
            if word in wordrate:
                wordrate[name] += 1
            else:
                wordsrate[name] = 1

    for name in words:
        for word in name:
            if wordsrate[word] > 1:
                name.remove(word)
        name = list(name)

    return words

videxts = ['.webm', '.flv', '.ogg', '.ogv', '.drc', '.mng', '.avi', '.mov', '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.mp4', '.m4p', '.m4v', '.mpg', '.mpeg', '.mp2', '.mpe', '.mpv', '.m2v', '.m4v', '.svi', '.3gp', '.3g2', '.mxf', '.roq', '.nsv', '.mkv']
subexts = ['.srt', '.smi', '.ssa', '.sub', '.sbv']

dirlist = os.listdir()

vids = []
subs = []
for d in dirlist:
    name, ext = os.path.splitext(d)
    if ext in videxts:
        vids.append(d)
    elif ext in subexts:
        subs.append(d)

#vidwords = []
#subwords = []
#for vid in vids:
    #vidwords = re.split('\W+', vid)
#for sub in subs:
    #subwords = re.split('\W+', sub)



#os.rename(sub, os.path.splitext(mindiffvid)[0] + os.path.splitext(sub)[1])

print(getuniques(vids))
