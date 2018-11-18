#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import os
import re
import shutil
import time
import asyncio
from proscan import scans
import inspect

basedir = r'\\192.168.120.200\f\原始文件'
basedir1 = r'\\192.168.120.200\f\cesiumData\cloud'
#for topdir in os.listdir(basedir):
#    os.chdir(basedir)
#    for subitems in os.listdir(topdir):
#        #print(subitems)
#        os.chdir(os.path.join(basedir, topdir))
#        attrs = ','.join(os.listdir(subitems))
#        print(subitems+':'+attrs)

#result = []
#for subdir in os.listdir(basedir):
#    result.append(subdir[:2])
#    idx = subdir.find('-')
#    if idx != -1:
#        result.append(subdir[idx+1:idx+3])


#for linename in os.listdir(basedir):
#    try:
#        dirs = os.listdir(os.path.join(basedir, linename))
#        os.chdir(os.path.join(basedir, linename))
#        dirs.index('pointcloud')
#    except Exception:
#        os.mkdir('pointcloud')
#    for dir in dirs:
#        if dir != 'pointcloud':
#            shutil.move(dir, 'pointcloud')





#for filepath in find_dfiles(basedir, 3):
#    if filepath.find('LAS_Image') != -1 and os.path.basename(filepath).find('conductor_Image.las') != -1:
#        pathlist = filepath.split('\\')
#        newpath = os.path.join(basedir1, pathlist[5], pathlist[6])
#        if not os.path.exists(newpath):
#            os.makedirs(newpath)
#        shutil.copy(filepath, newpath)


#with open(r'c:\Users\E450\Desktop\11.txt', 'w') as f:
#    for filepath in find_dfiles(basedir, 3):
#        f.writelines(filepath)
#        f.writelines('\r\n')
#    #print(filepath)




#'''瞬时切片目录整理'''
#
#pathdict = {}
#
#
#for i in scans(basedir, 2):
#    if i.find('瞬时切片') != -1:
#        #print(i)
#        for k in scans(i.replace('瞬时切片', '瞬时工况分析报告new')):
#            #print(k)
#            os.path.split(k)
#            pathdict.setdefault(os.path.split(k)[1], k)
#        for j in scans(i, 0):
#            #print(j)
#            dlist = j.split('\\')
#            #print(dlist[-1])
#
#for file in scans(basedir, 2):
#    if file.find('瞬时切片') != -1:
#        with os.scandir(file) as it:
#            for entry in it:
#                v = pathdict.get(entry.name+'.las')
#                rindex = v.rfind('\\')
#                #print(entry.path, v[:rindex].replace('原始文件', '重切瞬时').replace('瞬时工况分析报告new\\', ''))
#                newpath = v[:rindex].replace('原始文件', '重切瞬时').replace('瞬时工况分析报告new\\', '')
#                if not os.path.exists(newpath):
#                    os.makedirs(newpath)
#                shutil.move(entry.path, newpath)
#                os.chdir(newpath)
#                for newdir in os.listdir(newpath):
#                    os.rename(newdir, 'DangerousPoint')







#print(pathdict)
#with open(r"c:\Users\E450\Desktop\test.txt", 'w') as f:
#    f.write(str(pathdict))
#
''''''


#with open(r'c:\Users\E450\Desktop\zuobiao.txt', 'w') as f:
#    for i in scans(basedir, None, 'f'):
#        if i.find('坐标') != -1:
#            f.writelines(i)
#            f.write('\r\n')


basedir = r'c:\Users\E450\Desktop\qq'


for dirname, subdirs, files in os.walk(basedir):
    for file in files:
        if re.search('杆塔坐标', file):
            newfile = open(os.path.join(dirname, 'new'+file), 'w')
            with open(os.path.join(dirname, file), 'r') as f:
                ulist = []
                for line in f:
                    if not line.strip():
                        continue
                    if line.split('\t')[6] not in ulist:
                        newfile.writelines(line)
                        ulist.append(line.split('\t')[6])
                        #print(line.split('\t')[6])
            newfile.close
