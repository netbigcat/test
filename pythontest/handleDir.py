#!/usr/bin/env python3


import os
import re
import shutil


quduan = re.compile(r'\d{4}-\d{4}')
for dir, subdirs, files in os.walk(r'f:/Download/result'):
    for file in files:
        if quduan.search(file):
            new_dir = os.path.join(dir, quduan.findall(file)[0])
            if os.path.exists(new_dir):
                shutil.move(os.path.join(dir, file), new_dir)
            else:
                os.mkdir(new_dir)
                shutil.move(os.path.join(dir, file), new_dir)



