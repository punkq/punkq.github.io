# -*- coding: utf-8 -*-
import os

def write_category(cat):
    strings = []
    strings.append('## {}'.format(cat.capitalize()))
    cat_path = os.path.join('docs', cat)

    for name in os.listdir(cat_path):
        if os.path.isfile(os.path.join(cat_path, name)):
            if name.endswith('.md'): 
                file_path = os.path.join(cat_path, name)
                file_title = name[:-3]
                strings.append('- [{}]({})'.format(file_title, file_path))
        else:
            strings.append('- {}'.format(name))
            for subname in os.listdir(os.path.join(cat_path, name)):
                if not subname.endswith('.md'): continue
                file_path = os.path.join(cat_path, name, subname)
                file_title = subname[:-3]
                strings.append('  - [{}]({})'.format(file_title, file_path))

    strings.append('\n')
    return '\n'.join(strings)

md = []
title = '# [Wellcome](#top)'
md.append(title)

cats = os.listdir('docs')
for cat in cats:
    md.append(write_category(cat))

md.append('### [Back to top](#top)')

with open('README.md', 'w') as  f:
    f.write('\n'.join(md))

