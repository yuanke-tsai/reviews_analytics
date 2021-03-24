#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:14:34 2021

@author: yuanke.tsai
"""

data = []
count =0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        #print(len(data))#，會印出清單1000000筆。運用％（餘數），使每1000筆再print！
        count += 1
        if count % 100000 == 0:
            print(len(data))        