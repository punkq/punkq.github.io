# -*- coding: utf-8 -*-
import os
import posixpath

def write_category(cat):
    strings = []
    strings.append('## {}'.format(cat.capitalize()))
    cat_path = os.path.join('docs', cat)

    for name in os.listdir(cat_path):
        if os.path.isfile(os.path.join(cat_path, name)):
            if name.endswith('.md'): 
                file_path = os.path.join(cat_path, name)
                file_path = file_path.replace(os.sep, posixpath.sep)
                file_title = name[:-3].capitalize().replace('_', ' ')
                strings.append('- [{}]({})'.format(file_title, file_path))
        else:
            strings.append('- {}'.format(name.capitalize().replace('_', ' ')))
            for subname in os.listdir(os.path.join(cat_path, name)):
                if not subname.endswith('.md'): continue
                file_path = os.path.join(cat_path, name, subname)
                file_path = file_path.replace(os.sep, posixpath.sep)
                file_title = subname[:-3].capitalize().replace('_', ' ')
                strings.append('  - [{}]({})'.format(file_title, file_path))

    strings.append('')
    return '\n'.join(strings)

md = []
title = '# [PunkQ\'s Notebook](#top)'
md.append(title)

cats = os.listdir('docs')
for cat in cats:
    md.append(write_category(cat))

md.append('### [Back to top](#top)')

with open('index.md', 'w') as  f:
    f.write('\n'.join(md))

