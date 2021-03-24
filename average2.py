# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:29:15 2021

@author: Moonseog
"""

import statistics as st

student_name = ['Kim','Seo','Lee','Park','Choi']
sub_name = ['Korean', 'English','Mathematics']
kor_score = [49,80,20,100,80]
eng_score = [43,60,85,30,90]
math_score = [49,82,48,50,100]

print(sub_name[0],": ",st.mean(kor_score))
print(sub_name[1],": ",st.mean(eng_score))
print(sub_name[2],": ",st.mean(math_score))

for i in range(len(student_name)):
    print(student_name[i],": ", (kor_score[i]+eng_score[i]+math_score[i]) / len(sub_name))
   
