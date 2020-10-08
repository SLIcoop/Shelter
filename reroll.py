#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from info import Info
from main import Gender

i = Info()
g = Gender()

l = f'{g.l}'
gen = (g.p," ",l," лет ",g.ch)


print("Выбери характеристику")
print("1.Фобия")
print("2.Здоровье")
print("3.Профессия")
print("4.Багаж")
print("5.Хобби")
print("6.Гендер")
print("7.Доп.инфа")

while True:
    choice = input("Выбери(1-7): ")

    if choice == '1':
        fob = i.fob
        f = open("newinfo.txt","w")
        f.writelines(fob)
        f.close()
    if choice == '2':
        fit = i.fit
        f = open("newinfo.txt","w")
        f.writelines(fit)
        f.close()
    if choice == '3':
        prof = i.prof
        f = open("newinfo.txt","w")
        f.writelines(prof)
        f.close()
    if choice == '4':
        bag = i.bag
        f = open("newinfo.txt","w")
        f.writelines(bag)
        f.close()
    if choice == '5':
        hob = i.hob
        f = open("newinfo.txt","w")
        f.writelines(hob)
        f.close()
    if choice == '6':
        f = open("newinfo.txt","w")
        f.writelines(gen)
        f.close()
    if choice == '7':
        info = i.dop_info 
        f = open("newinfo.txt","w")
        f.writelines(info)
        f.close()
    break
