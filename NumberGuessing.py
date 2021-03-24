# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 16:54:22 2021

@author: Moonseog
"""

import random

secret_number = random.randint(0, 100)
success = False
for i in range(1,10):
    guessing_number = int(input("[{0}]Input guessing number: ".format(i)))
    if secret_number == guessing_number:
        success = True
        break
    elif secret_number > guessing_number:
        print("추측한 값보다 큽니다.")
    else: 
        print("추측한 값보다 작습니다.")
if success:
    print("success!!")
else:
    print("Fail!!")
    