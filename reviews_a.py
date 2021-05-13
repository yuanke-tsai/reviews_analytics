#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:14:34 2021

@author: yuanke.tsai
"""
#新增篩選功能
#字數篩選
#特徵篩選>>清單快寫法
#新增字典查詢
#新增計時
import time

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

#文字查詢
#計時
start_time = time.time()
wc = {} # word count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] >= 1000000:
        print(word, wc[word])
end_time = time.time()

print('run 留言花了：', end_time - start_time, '秒')
print('字典長度：', len(wc))

while True:
    user_input = input('請問想查詢什麼字？')
    if user_input == 'q':
        print('離開查詢')
        break
    if user_input in wc:
        print(user_input, '出現過次數為：', wc[user_input])
    else:
        print('查無此')





