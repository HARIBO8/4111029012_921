#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 16:01:14 2023

@author: keigo
"""

import os
import shutil
import time

os.mkdir('CS')

os.mkdir('homework')

path = './homework/homework.txt'
with open(path, 'w') as f:
    f.write('內容為：4111029012_長谷川慶伍')
f.close()

f = open('./homework/homework.txt', 'r')
content = f.read()
print(content)
file_size = os.path.getsize('./homework/homework.txt')
print(f'文件大小: {file_size}字節')
modification_time = os.path.getmtime('./homework/homework.txt')
print(f'最後修改時間: {modification_time}')
formatted_time = time.ctime(modification_time)
print(f'最後修改時間(人類可讀格式): {formatted_time}')

shutil.rmtree('./homework') 

f.close()