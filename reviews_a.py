#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:14:34 2021

@author: yuanke.tsai
"""
#新增篩選功能
#字數篩選
#特徵篩選>>清單快寫法

data = []

with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)

base = []
total_len = 0
for base in data:
    total_len = total_len + len(base)

#字數篩選        
new = []
for base in data:
    if len(base) < 100:
        new.append(base)

#特徵篩選>>清單快寫法
good = [base for base in data if 'good' in base]


print('總留言字數：', total_len)
print('留言總數：', len(data))
print('平均留言個數：', total_len / len(data))
print('留言字數小於一百字：', len(new), '筆')
print('留言中包含good之數量：', len(good), '筆')
