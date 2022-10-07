# -*- coding: utf-8 -*-
import os
import posixpath

def titlize(title):
    words = title.split('_')
    words = [w.capitalize() for w in words]
    return ' '.join(words)

def write_category(cat):
    strings = []
    strings.append('## {}'.format(cat.capitalize()))
    cat_path = os.path.join('docs', cat)

    for name in os.listdir(cat_path):
        if os.path.isfile(os.path.join(cat_path, name)):
            if name.endswith('.md'): 
                file_path = os.path.join(cat_path, name)
                file_path = file_path.replace(os.sep, posixpath.sep)
                strings.append('- [{}]({})'.format(titlize(name[:-3]), file_path))
        else:
            strings.append('- {}'.format(titlize(name)))
            for subname in os.listdir(os.path.join(cat_path, name)):
                if not subname.endswith('.md'): continue
                file_path = os.path.join(cat_path, name, subname)
                file_path = file_path.replace(os.sep, posixpath.sep)
                file_title = titlize(subname[:-3])
                strings.append('  - [{}]({})'.format(file_title, file_path))

    strings.append('')
    return '\n'.join(strings)

md = []
title = '# [PunkQ\'s Notebook](#top)'
md.append(title)

cats = os.listdir('docs')
cats.reverse()
for cat in cats:
    md.append(write_category(cat))

md.append('### [Back to top](#top)')

with open('index.md', 'w') as  f:
    f.write('\n'.join(md))

