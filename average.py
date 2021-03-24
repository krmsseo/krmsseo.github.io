# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 09:55:22 2021

@author: Moonseog
"""
student_name = ['Kim','Seo','Lee','Park','Choi']
sub_name = ['Korean', 'English','Mathematics']
kor_score = [49,80,20,100,80]
eng_score = [43,60,85,30,90]
math_score = [49,82,48,50,100]
score = [kor_score,eng_score,math_score]

sub_avg = []
num_stduent = len(student_name)
for subject in score:
    sum = 0
    for sub_score in subject:
        sum = sum + sub_score
    sub_avg.append(sum/num_stduent)
print("Subject Average: ",sub_avg)

student_avg = []
num_subject = len(sub_name)
for i in range(num_stduent):
    sum = 0
    for j in range(num_subject):
        sum += score[j][i]
    student_avg.append(sum/num_subject)
print("Student Average: ", student_avg)
