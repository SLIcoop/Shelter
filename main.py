#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from info import Info

#random gender gender, year and childfree
class Gender:
	def __init__(self):
		self.p = random.choice(["Женщина", "Мужчина"])
		self.l = random.randint(18,80)
		self.ch = random.choice(["Чайлдфри","Не чайлдфри"])

class Skin:
    def __init__(self):
        self.v = random.randint(30, 150)
        self.r = random.randint(150, 210)

g = Gender()
i = Info()

#format int to string
l = f'{g.l}'
gen = (g.p," ",l," лет ",g.ch)

s = Skin()
v = f'{s.v}'
r = f'{s.r}'

#create .txt file
file1 = open("information.txt","w")
file1.write("Гендер: ")
file1.writelines(gen)
file1.write("\n")
file1.write("Профессия: ")
file1.writelines(i.prof)
file1.write("\n")
file1.write("Здоровье: ")
file1.writelines(i.fit)
file1.write("\n")
file1.write("Рост: ")
file1.writelines(r)
file1.write("\n")
file1.write("Вес: ")
file1.writelines(v)
file1.write("\n")
file1.write("Хобби: ")
file1.writelines(i.hob)
file1.write("\n")
file1.write("Фобия: ")
file1.writelines(i.fob)
file1.write("\n")
file1.write("Дополнительная информация: ")
file1.writelines(i.dop_info)
file1.write("\n")
file1.write("Характер: ")
file1.writelines(i.chert)
file1.write("\n")
file1.write("Багаж: ")
file1.writelines(i.bag)
file1.write("\n")
file1.write("Карта действия 1: ")
file1.writelines(i.card)
file1.write("\n")
file1.write("Карта действия 2: ")
file1.writelines(i.card_two)
file1.close()
