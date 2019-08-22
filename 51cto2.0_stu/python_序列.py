#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "likeu"
# Date: 2019-08-21

#序列
msg="123456789"
print(msg[0])
print(msg[3])
print(msg[-2])
print(msg)
print(msg[0:3])# 截止到三，不包括三。
print(msg[1:6])#截止到六，不包括六。
print(msg[-1:])
print(msg[-3:])
print(msg[::2])
print(msg[-2::-2])
print(msg[::-1])
msg = 'helloworld'
#创建enumerate对象
items = enumerate(msg)
#遍历enumerate对象
for item in items:
    print(item)

msg = 'helloworld'
for tindex, tvalue in enumerate(msg):
    print(tindex, tvalue)
liebiao=[1,2,3,4]
print(liebiao[0:7:2])