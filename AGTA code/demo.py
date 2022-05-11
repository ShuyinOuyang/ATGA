#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 21/03/2022 14:24
# @Author  : Shuyin Ouyang
# @File    : demo.py

import matplotlib.pyplot as plt
x_cords = range(0, 100)
y_cords = [(19-0.02*x)/(26-0.03*x) for x in x_cords]

plt.plot(x_cords, y_cords)
plt.show()