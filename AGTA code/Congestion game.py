#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 21/04/2022 17:02
# @Author  : Shuyin Ouyang
# @File    : Congestion game.py

import copy

# setting
# number of players
N = 3
# s v1 v2 v3 v4 v5 t
matrix = [
    [(),(7,2,7), (3,4,6), (8,4,6), (), (), ()], #s
    [(), (), (), (), (3,6,7), (), ()], #v1
    [(), (6,5,5), (), (1,9,8), (3,5,9), (4,5,8), ()], #v2
    [(),(),(),(),(),(4,3,4),()], #v3
    [(),(),(),(),(),(),(9,8,6)], #v4
    [(),(),(),(),(),(),(4,8,4)] #v5
]

# matrix = [
#     [(),(7,4,8), (0,3,6), (3,6,7), ()], #s
#     [(), (), (), (), (1,3,4)], #v1
#     [(), (4,3,5), (), (4,2,6), ()], #v2
#     [(),(),(),(),(9,7,9)] #v3
# ]

# find all path from s->t
def find_path(matrix, res, path, pos=0):
    if len(path) != 0:
        if path[0] == 0 and path[-1] == len(matrix[0])-1:
            res.append(path)
            return

    for i in range(len(matrix[pos])):
        if len(matrix[pos][i]) != 0:
            find_path(matrix, res, path + [i], pos=i)

all_path = []
path = [0]
find_path(matrix, all_path, path, pos=0)

# all combination of players' paths
min_cost = float('inf')
all_combination = []
dict={'A': [], 'B': [], 'C': [], 'cost':0}


for i in range(len(all_path)):
    for j in range(len(all_path)):
        for k in range(len(all_path)):
            tmp = [i,j,k]
            if tmp not in all_combination:
                all_combination.append(tmp)

# calculate the cost
all_cost = []
for i in range(len(all_combination)):
    dict_temp = {}
    cost = [0 for _ in range(N)]
    for k in range(len(all_combination[i])):
        path_ = all_path[all_combination[i][k]]
        for j in range(len(path_)):
            if j != len(path_) - 1:
                if (path_[j],path_[j+1]) not in dict_temp:
                    dict_temp[(path_[j],path_[j+1])] = 1
                else:
                    dict_temp[(path_[j], path_[j + 1])] += 1
    for n in range(N):
        path_ = all_path[all_combination[i][n]]
        for j in range(len(path_)):
            if j != len(path_) - 1:
                cost[n] += matrix[path_[j]][path_[j+1]][dict_temp[(path_[j],path_[j+1])]-1]
    dict_temp['cost'] = cost
    all_cost.append(dict_temp)

res = []
for i in range(len(all_combination)):
    dict_temp = {}
    dict_temp['id'] = all_combination[i]
    for j in range(N):
        dict_temp['player %s'%(j+1)] = all_path[all_combination[i][j]]
    dict_temp['cost'] = all_cost[i]['cost']
    res.append(dict_temp)


for dic in res:
    # fix other two player
    for i in range(N):
        flag = True
        # change the stragegy
        combination = copy.deepcopy(dic['id'])
        for j in range(len(all_path)):
            combination[i] = j
            if dic['cost'][i] > res[all_combination.index(combination)]['cost'][i]:
                dic['NE'] = False
                flag = False
                break
        if flag == False:
            break
    if 'NE' not in dic:
        dic['NE'] = True
    if dic['NE'] == True:
        print(dic)