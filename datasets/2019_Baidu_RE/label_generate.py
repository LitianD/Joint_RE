#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：Joint_RE -> label_generate
@Author ：Litian. Zhang
@Date   ：2020/7/3 15:25
==================================================
"""
import json

data_path = "D:\\NLP_Datasets\\all_50_schemas"
out_path = "rel2id.json"
f = open(data_path, 'r', encoding='UTF-8')
line = f.readline()
num = 0
d1 = {}
d2 = {}
while line:
    temp = json.loads(line)
    d1[str(num)] = temp["predicate"]
    s = temp["predicate"]
    d2[s] = num
    num = num + 1
    line = f.readline()
f.close()
rel2id_list = [d1, d2]

with open(out_path, 'w', encoding='utf-8') as file_obj:
    json.dump(rel2id_list, file_obj, ensure_ascii=False, indent=1)