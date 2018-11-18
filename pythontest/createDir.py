#!/usr/bin/env python3


import os
import re


for parent, dirnames, filenames in os.walk(r'h:/new'):
    for file in filenames:
        #dirpath = os.path.join(parent, file)
        try:
            if re.search(r'buildings', file):
                dirpath = os.path.join(parent, 'building')
                os.mkdir(dirpath)
            if re.search(r'conductor', file):
                dirpath = os.path.join(parent, 'conductor')
                os.mkdir(dirpath)
            if re.search(r'high_vegetation', file):
                dirpath = os.path.join(parent, 'vegetation(high)')
                os.mkdir(dirpath)
            if re.search(r'lake', file):
                dirpath = os.path.join(parent, 'lake')
                os.mkdir(dirpath)
            if re.search(r'other', file):
                dirpath = os.path.join(parent, 'other')
                os.mkdir(dirpath)
            if re.search(r'river', file):
                dirpath = os.path.join(parent, 'river')
                os.mkdir(dirpath)
            if re.search(r'road', file):
                dirpath = os.path.join(parent, 'road')
                os.mkdir(dirpath)
            if re.search(r'scissors_crossing', file):
                dirpath = os.path.join(parent, 'crossing')
                os.mkdir(dirpath)
            if re.search(r'shield_wire', file):
                dirpath = os.path.join(parent, 'wire')
                os.mkdir(dirpath)
            if re.search(r'structures', file):
                dirpath = os.path.join(parent, 'structures')
                os.mkdir(dirpath)
            if re.search(r'DangerousPoint.las', file):
                dirpath = os.path.join(parent, 'DangerousPoint')
                os.mkdir(dirpath)
        except FileExistsError as e:
            print(e)

