# -*- coding: utf-8 -*-
import os

def write_category(cat):
    strings = []
    strings.append('## {}'.format(cat.capitalize()))

    for root, dirs, files in os.walk(os.path.join('docs', cat), topdown=False):
        for name in files:
            if not name.endswith('.md'): continue
            file_path = os.path.join(root, name)
            file_title = name[:-3]
            strings.append('- [{}]({})'.format(file_title, file_path))
        for dir_name in dirs:
            strings.append('- {}'.format(dir_name))
            for name in os.listdir(os.path.join(root, dir_name)):
                if not name.endswith('.md'): continue
                for name in os.listdir(os.path.join(root, dir_name)):
                    file_path = os.path.join(root, dir_name, name)
                    file_title = name[:-3]
                    strings.append('  - [{}]({})'.format(file_title, file_path))


    return '\n'.join(strings)

md = []
title = '# Wellcome'
md.append(title)

cats = os.listdir('docs')
for cat in cats:
    md.append(write_category(cat))

md.append('### [Back to top](Welcome)')

with open('README.md', 'w') as  f:
    f.write('\n'.join(md))

