#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 17/02/2022 22:23
# @Author  : Shuyin Ouyang
# @File    : assignment1.py

from scipy.optimize import linprog
import numpy as np

print('Prime -----------------------')
# A = [[3,3,9,6,2],
#      [7,8,4,5,3],
#      [1,2,5,6,4],
#      [1,4,4,5,9],
#      [4,7,7,8,3]]

A = [
    [2,9,4],
    [7,0,3]
]

A = [
    [2,1,1],
    [3,1,4]
]

A = np.array(A)
# A_ub = np.hstack((0-A, np.ones((len(A), 1))))
A_ub = -A
# A_eq = np.array([[1, 1, 1, 0]])
# A_eq = np.array([[0,0,0,0]])
# b_ub = np.zeros(len(A))
b_ub = np.array([-5,-3])
b_eq = [1]
c = [-8,-6,-4]

x_bounds = (0, None)
x6_bounds = (None, None)
res = linprog(c, A_ub=A_ub, b_ub=b_ub, #A_eq=A_eq, b_eq=b_eq, \
              bounds=[x_bounds, x_bounds, x6_bounds], \
              method='simplex')
print(res)

# print('Another solution-------------------')
#
# res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, \
#               bounds=[x_bounds, x_bounds, x_bounds, x_bounds, x_bounds, x6_bounds], \
#               method='revised simplex')
# print(res)

# print('Dual -----------------------')
# A = np.array(A)
# A_ub = np.hstack((A, -np.ones((5, 1))))
# A_eq = np.array([[1, 1, 1, 1, 1, 0]])
# b_ub = np.zeros(5)
# b_eq = [1]
# c = [0,0,0,0,0,1]
# x_bounds = (0, 1)
# x6_bounds = (None, None)
# res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, \
#               bounds=[x_bounds, x_bounds,x_bounds, x6_bounds], \
#               method='revised simplex')
# print(res)