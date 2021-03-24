# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:42:11 2021

@author: Moonseog
"""

for x in range(2,10,4):
    for y in range(1,10):
        for z in range(0,4):
            print(x+z,"X",y,"= ",(x+z)*y, end='  ')
        print()
    print()