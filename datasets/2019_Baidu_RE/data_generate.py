#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：Joint_RE -> data_generate
@Author ：Litian. Zhang
@Date   ：2020/7/3 14:57
==================================================
"""
import json

data_path = "D:\\NLP_Datasets\\train_data.json"
out_path = "train_data.json"
json_list = []
f = open(data_path, 'r', encoding='UTF-8')
line = f.readline()
while line:
    temp = json.loads(line)
    new = {"text": temp["text"]}

    temp_lists = []
    for item in temp["spo_list"]:
        temp_list = [item["object"], item["predicate"], item["subject"]]
        temp_lists.append(temp_list)
    new["triple_list"] = temp_lists

    json_list.append(new)
    line = f.readline()
f.close()

with open(out_path, 'w', encoding='utf-8') as file_obj:
    json.dump(json_list, file_obj, ensure_ascii=False, indent=1)



