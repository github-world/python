#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2019-08-19
i = 1
while i < 5:
    print(i)
    i += 1

idata = ""
while idata !='q':
    idata = input('Enter:')

while True:
    #读取输入
    idata = input("1:")
    if idata == 'q':
        print('catch q!')
        #输入q,退出当前循环。
        break


