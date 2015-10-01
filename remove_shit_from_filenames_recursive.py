import os
from os.path import join, getsize

path = input('Path: ')
shit = input('Shit: ')

to_be_renamed = []
for root, dirs, files in os.walk(path):
    for f in files:
        if shit in f:
            #print('AAAA!! FOUND SHIT!!!1')
            new_f = f.replace(shit, '')
            to_be_renamed.append(join(root, f), join(root, new_f))

print('Following files are going to be renamed: ')
for f in to_be_renamed:
    print(os.path.basename(f[0]) + ' -> ' + os.path.basename(f[1]))

proceed = input('Are you willing to proceed (y/n)? ')
if proceed == 'y':
    for f in to_be_renamed:
        os.rename(f[0], f[1])
    print('Done.')
else:
    print('Rename aborted.')
