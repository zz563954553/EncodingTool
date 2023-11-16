#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@Author         : Mr Z
@Project        : auto
@File           : Base64Coding.py
@Software       : PyCharm
@Time           : 2023-02-01 13:53
@Description    : 
"""
from tqdm import trange
from base64 import b64encode
codedatas = list()
pre_file_path = r"C:\Users\Administrator\Desktop\111.txt"
file_path = r"C:\Users\Administrator\Desktop\222.txt"
with open(pre_file_path, "r", encoding="utf-8") as f:
    pre_datas = f.readlines()
with open(file_path, "a+", encoding="utf-8") as f:
    for i in trange(0, len(pre_datas)):
        data = pre_datas[i].strip('\n')
        codedata = b64encode(data.encode("utf-8")).decode("utf-8")+"\n"
        f.write(codedata)
