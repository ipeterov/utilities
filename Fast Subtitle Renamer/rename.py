import os, re

def find_season_and_episode(f):
    for pattern in patterns:
        result = re.search(pattern, f.lower())
        if result:
            result = result.group()
            break
    else:
        return None

    if len(result) == 3:
        season, episode = int(result[0]), int(result[1:3])
    else:
        season, episode = [int(x) for x in re.findall('\d+', result)]

    return season, episode

def sub_or_vid(f):
    name, ext = os.path.splitext(f)
    if ext in subexts:
        return 'sub'
    elif ext in videxts:
        return 'vid'
    else:
        return None

videxts = open('videxts.txt', 'r').read().splitlines()
subexts = open('subexts.txt', 'r').read().splitlines()
patterns = open('patterns.txt', 'r').read().splitlines()

path = input('Path: ')

files = os.listdir(path)

vids = {}
subs = {}
for f in files:
    se = find_season_and_episode(f)
    t = sub_or_vid(f)

    if t == 'sub':
        subs[se] = f
    elif t == 'vid':
        vids[se] = f

to_be_renamed = []
for key in vids:
    if key in subs:
        to_be_renamed.append([subs[key], os.path.splitext(vids[key])[0] + os.path.splitext(subs[key])[1]])
to_be_renamed.sort()

print('Following files are going to be renamed: ')
for f in to_be_renamed:
    print(f[0] + ' -> ' + f[1])

proceed = input('Are you willing to proceed (y/n)? ')
if proceed == 'y':
    for f in to_be_renamed:
        os.rename(os.path.join(path, f[0]), os.path.join(path, f[1]))
    print('Done.')
else:
    print('Rename aborted.')

