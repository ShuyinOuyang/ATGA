#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 03/05/2022 11:31
# @Author  : Shuyin Ouyang
# @File    : 3d.py

import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建画布
fig = plt.figure(figsize=(12, 8),
                 facecolor='lightyellow'
                 )

# 创建 3D 坐标系
ax = fig.gca(fc='whitesmoke',
             projection='3d'
             )  # 二元函数定义域平面
x = np.linspace(0, 9, 9)
y = np.linspace(0, 9, 9)
X, Y = np.meshgrid(x, y)

# -------------------------------- 绘制 3D 图形 --------------------------------
# 平面 z=4.5 的部分
ax.plot_surface(X,
                Y,
                Z=5-2*X-Y,
                color='r',
                alpha=0.6
                )

# 平面 y=4.5 的部分
ax.plot_surface(X,
                Y,
                Z=(3-3*X-Y)/4,
                color='b',
                alpha=0.6
                )

ax.plot_surface(X=0,
                Y=Y,
                Z=X,
                color='g',
                alpha=0.6
                )

ax.plot_surface(X=X,
                Y=0,
                Z=Y,
                color='y',
                alpha=0.6
                )

# 平面 x=4.5 的部分
# ax.plot_surface(X=X * 0 + 4.5,
#                 Y=Y,
#                 Z=X,
#                 color='r',
#                 alpha=0.6
#                 )
# --------------------------------  --------------------------------
# 设置坐标轴标题和刻度
ax.set(xlabel='X',
       ylabel='Y',
       zlabel='Z',
       xlim=(0, 9),
       ylim=(0, 9),
       zlim=(0, 9),
       xticks=np.arange(0, 10, 2),
       yticks=np.arange(0, 10, 1),
       zticks=np.arange(0, 10, 1)
       )

# 调整视角
ax.view_init(elev=15,  # 仰角
             azim=60  # 方位角
             )

# 显示图形
plt.show()