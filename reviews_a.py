#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:14:34 2021

@author: yuanke.tsai
"""

data = []

with open('reviews.txt', 'r') as file:
    for line in file:
        data.append(line)

base = []
total_len = 0
for base in data:
    total_len = total_len + len(base)

print('總留言字數：', total_len)
print('留言總數：', len(data))
print('平均留言個數：', total_len / len(data))