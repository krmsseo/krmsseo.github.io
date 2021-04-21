# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 16:49:39 2021

@author: Moonseog
"""

"""
입력으로 높이를 받아
별표 삼각형 찍기
"""
height = int(input("Input Height: "))

for i in range(height-1, -1,-1):
    print(' '*i, end='')
    print('*'*(height-i),end='')
    print('*'*(height-(i+1)))

