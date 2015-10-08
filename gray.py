#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

i = 0
liste = []
gray_liste = []
 
x = int(input("Bir sayi giriniz: "))
while x >= 1 :
    i += 1
    liste.append(int(x%2))
    x = x / 2
 
liste.reverse()

gray_liste.append(liste[0])


for j in range(0, len(liste)-1):
   if liste[j] == liste[j+1]:
       gray_liste.append('0')
   else:
        gray_liste.append('1')

for oge in gray_liste:
     sys.stdout.write(str(oge)+"")
    
