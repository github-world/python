#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "likeu"
# Date: 2019-08-20

#人类模板
class People():
    def __init__(self, name, age, bullet):
        self.name = name
        self.age = age
        self.gnu = None
        self.bullet = bullet
    def display_info(self):
        print("动作--查看信息")
        print("姓名："+self.name)
        print("年龄"+ str(self.age))

        if self.gnu:
            print("枪械:"+self.gnu.name)
        else:
            print("枪械：无")
        print("剩余子弹:" + str(self.bullet))
        print("")
    def take_gnu(self, gnu_name): #拿枪
        print("动作--拿枪")
        if self.gnu:
            print("手里已经有"+self.gnu.name)
        else:
            self.gnu = Gnu(gnu_name)
            print("获得一把"+self.gnu.name)
        print("")
    def zhuang(self):
        print("动作--装弹")
        hao = self.gnu.inst_bullet(self)
        if hao == 3:
            print("子弹已经是满的，无需装载")
        elif hao == 9:
            print("剩余子弹数不够装满")
        else:
            self.bullet = self.bullet - hao
            print("已经装子弹"+str(hao))
        print("")
    def fashe(self):
        print("动作--发射子弹")
        self.gnu.emission_bullet
#装子弹，打枪
class Gnu():
    def __int__(self,name):
        self.name = name
        self.bullet =0
    def inst_bullet(self,last_bullet):
        if self.bullet ==20:
            return 3
        else:
            linshi_bullet = 20 - self.bullet
            if last_bullet > linshi_bullet:
                self.bullet = 20
                return  linshi_bullet
            else:
                return 9
    def emission_bullet(self):
        if self.bullet>0:
            self.bullet = self.bullet -1
            print("发射了一颗了弹")
        else:
            print("没有子弹了")
        print("")
#初始化和查看信息
ren=People("张三", 13, 255)
ren.display_info()
ren.take_gnu("AK47")
ren.fashe()
ren.zhuang()
ren.fashe()
ren.fashe()
ren.zhuang()
ren.zhuang()
ren.display_info()