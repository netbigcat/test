#!/usr/bin/env python3


import os
import re
import shutil


def formatdirectory(fdir):
    for dirname, subdirs, files in os.walk(fdir):
    #for dirname, subdirs, files in os.walk(r'Z:\葛南线\肤色切片'):
        for subdir in subdirs:
            subpath = os.path.join(dirname, subdir)
            if re.search(r'(Image)|(DangerousPoint)', subdir) and subdir != 'LAS_Image':
                quduan = re.search(r'(\d{1,4}\+\d-\d{1,4}\+\d)|(\d{1,4}\+\d-\d{1,4})|(\d{1,4}-\d{1,4}\+\d)|(\d{1,4}-\d{1,4})', subdir).group()
                qdpath = os.path.join(dirname, quduan)
                #print(subpath)
                if not re.search(quduan, dirname):
                    if not os.path.exists(qdpath):
                        os.makedirs(qdpath)
                    newsubdir = subdir.replace('_Image', '')
                    newsubdir = re.sub(r'.*((\d{1,4}\+\d-\d{1,4}\+\d)|(\d{1,4}\+\d-\d{1,4})|(\d{1,4}-\d{1,4}\+\d)|(\d{1,4}-\d{1,4}))_', '', newsubdir)
                    if newsubdir == 'shield_wire':
                        newsubdir = 'wire'
                    elif newsubdir == 'high_vegetation':
                        newsubdir = 'vegetation(high)'
                    elif newsubdir == 'scissors_crossing(down)':
                        newsubdir = 'crossing(down)'
                    elif newsubdir == 'scissors_crossing(up)':
                        newsubdir = 'crossing(up)'
                    elif newsubdir == 'bridges':
                        newsubdir = 'bridge'
                    elif newsubdir == 'temporary_building':
                        newsubdir = 'building(temp)'
                    elif newsubdir == 'insulator_string':
                        newsubdir = 'insulator'
                    newsubpath = os.path.join(dirname, newsubdir)
                    os.chdir(dirname)
                    os.rename(subdir, newsubdir)
                    shutil.move(newsubpath, qdpath)






dirs = [

r"\\192.168.120.200\f\原始文件\数据问题\没赋色，重切\凤定2858线\切片",

]



for dir in dirs:
    formatdirectory(dir)
