#!/usr/bin/env python3


import os
import re


basedir = r'c:\Users\E450\Desktop\ww'


for dir, subdirs, files in os.walk(r'\\192.168.120.200\f\原始文件'):
    if re.search(r'瞬时工况.*\\\d{1,4}-\d{1,4}', dir):
        qdpattern = re.compile(r'^\d{1,4}-\d{1,4}\.')
        filepath = 0
        for file in files:
            if qdpattern.search(file):
                filepath = os.path.join(dir, file)
                break
            elif file == '1.txt':
                filepath = os.path.join(dir, file)
        if filepath:
            #print(filepath)
            tempdir = filepath.split('\\')
            newfile = tempdir[4] + tempdir[5] + tempdir[6] + tempdir[7] + '.txt'
            shunfile = os.path.join(basedir, newfile)
            # print(newfile)
            with open(shunfile, 'a') as f:
                for line in open(filepath, 'r'):
                    f.writelines(line)
                    # f.write('\r\n')
    for file in files:
        filepath = os.path.join(dir, file)
#        if re.search(r'瞬时工况.*\\\d{1,4}-\d{1,4}\.txt', filepath):
#            #print(filepath)
#            tempfile = filepath.split('\\')
#            newfile = tempfile[2] + tempfile[3] + tempfile[4] + '.txt'
#            shunfile = os.path.join(basedir, newfile)
#            #print(newfile)
#            with open(shunfile, 'a') as f:
#                for line in open(filepath, 'r'):
#                    f.writelines(line)
#                    #f.write('\r\n')
        if re.search(r'交跨.*\\1\.txt', filepath):
            #print(filepath)
            tempfile = filepath.split('\\')
            newfile = tempfile[4] + tempfile[5] + tempfile[6] + tempfile[7] + '.txt'
            kuafile = os.path.join(basedir, newfile)
            #print(newfile)
            with open(kuafile, 'a') as f:
                for line in open(filepath, 'r'):
                    f.writelines(line)
                    #f.write('\r\n')
        elif re.search(r'杆塔坐标.*\\[a-zA-Z]{2,6}\d{0,2}.((\d{1,4}\+\d-\d{1,4}\+\d)|(\d{1,4}\+\d-\d{1,4})|(\d{1,4}-\d{1,4}\+\d)|(\d{1,4}-\d{1,4}))\.txt', filepath):
            #print(filepath)
            tempfile = filepath.split('\\')
            newfile = tempfile[4] + tempfile[5] + tempfile[6] + tempfile[7] + '.txt'
            zuobiaofile = os.path.join(basedir, newfile)
            #print(newfile)
            with open(zuobiaofile, 'a') as f:
                for line in open(filepath, 'r'):
                    f.writelines(line)
                    #f.write('\r\n')


#for dirname, subdirs, files in os.walk(basedir):
#    for file in files:
#        if re.search('杆塔坐标', file):
#            newfile = open(os.path.join(dirname, 'new'+file), 'w')
#            with open(os.path.join(dirname, file), 'r') as f:
#                ulist = []
#                for line in f:
#                    if not line.strip():
#                        continue
#                    if line.split('\t')[6] not in ulist:
#                        newfile.writelines(line)
#                        ulist.append(line.split('\t')[6])
#                        #print(line.split('\t')[6])
#            newfile.close



