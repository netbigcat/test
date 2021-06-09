#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import datetime, proscan, os



today = str(datetime.date.today())
wordlist = []
for dirName in proscan.scans(r'c:\Users\FENG\OneDrive\English\zhimi', 0, 'f'):
    if os.path.splitext(dirName)[1] == '.word':
        with open(dirName, 'r', encoding='utf-8') as cf:
            for line in cf.readlines():
                wordlist.append(line.split('\t')[0])
        print(wordlist)


f = open(r'c:\Users\FENG\Desktop\zhimiword-' + today + '.word', 'r', encoding='utf-8')
nf = open(r'c:\Users\FENG\OneDrive\English\zhimi\zhimiword-' + today + '.word', 'w', encoding='utf-8')
for line in f.readlines():
    if line.split('\t')[0] not in wordlist:
        nf.writelines(line)
        #nf.writelines('\n')
        nf.flush()

f.close()
nf.close()
