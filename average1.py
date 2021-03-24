# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:19:38 2021

@author: Moonseog
"""
import numpy as np

student_name = ['Kim','Seo','Lee','Park','Choi']
sub_name = ['Korean', 'English','Mathematics']
kor_score = [49,80,20,100,80]
eng_score = [43,60,85,30,90]
math_score = [49,82,48,50,100]

score = np.array([kor_score,eng_score,math_score])
student_avg = list(score.mean(axis=0))
subject_avg = list(score.mean(axis=1))
print(student_avg)
print(subject_avg)