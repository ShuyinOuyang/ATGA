#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 21/04/2022 11:04
# @Author  : Shuyin Ouyang
# @File    : VCG.py

# VCG settings:
# input = ['0 9 6 10 16 20 17 24',
#       '0 5 8 9 14 21 15 23',
#       '0 1 11 1 12 2 12 13']

input = ['0 5 1 6 12 15 13 16',
      '0 3 4 6 18 17 17 22',
      '0 9 7 5 17 19 18 20']

# input = ['0 4 11 15',
#          '0 7 8 16',
#          '0 6 10 17']



valuation = []
column_1 = ['', '1', '2', '3', '1 2', '1 3', '2 3', '1 2 3']
column_2 = ['0', '1', '2', '3']


for line in input:
    content = line.split()
    valuation_bidder = []
    for i in range(len(content)):
        valuation_bidder.append(float(content[i]))
    valuation.append(valuation_bidder)

if len(valuation[0]) == len(column_1):
    column = column_1
else:
    column = column_2

test = ['A', 'B', 'C']

res = []
combination = []


def backtrack(nums, tmp):
    if len(tmp) == 3:
        res.append(tmp)
        return
    for i in range(len(nums)):
        backtrack(nums, tmp + [nums[i]])


backtrack(test, [])
for i in range(len(res)):
    tmp = {'A':[], 'B':[], 'C':[]}
    for j in range(len(res[i])):
        tmp[res[i][j]].append(j+1)
    sum = 0
    for j, v in enumerate(tmp):
        if column == column_1:
            r = column.index(' '.join(str(n) for n in tmp[v]))
        else:
            r = column.index('%s' % (len(tmp[v])))
        sum += valuation[j][r]
    tmp['sum_price'] = sum
    combination.append(tmp)

# max sum price
max = 0
best_combination_index = -1
max_without = [0,0,0]
best_combination_index_without = [-1, -1, -1]
for i in range(len(combination)):
    if combination[i]['sum_price'] > max:
        max = combination[i]['sum_price']
        best_combination_index = i

    if combination[i]['sum_price'] > max_without[0] and combination[i]['A'] == []:
        max_without[0] = combination[i]['sum_price']
        best_combination_index_without[0] = i

    if combination[i]['sum_price'] > max_without[1] and combination[i]['B'] == []:
        max_without[1] = combination[i]['sum_price']
        best_combination_index_without[1] = i

    if combination[i]['sum_price'] > max_without[2] and combination[i]['C'] == []:
        max_without[2] = combination[i]['sum_price']
        best_combination_index_without[2] = i
if column == column_1:
    print('VCG allocation:', combination[best_combination_index])
else:
    for i,v in enumerate(combination[best_combination_index]):
        if v != 'sum_price':
            combination[best_combination_index][v] = [len(combination[best_combination_index][v])]
    print('VCG allocation:', combination[best_combination_index])
print('VCG price:', max)
sum_without = [0, 0, 0]
for j, v in enumerate(combination[best_combination_index]):
    if v == 'sum_price':
        continue
    if column == column_1:
        r = column.index(' '.join(str(n) for n in combination[best_combination_index][v]))
    else:
        r = column.index('%s' % (len(combination[best_combination_index][v])))
    # print(valuation[j][r])
    if v == 'A':
        sum_without[1] += valuation[j][r]
        sum_without[2] += valuation[j][r]
    elif v == 'B':
        sum_without[0] += valuation[j][r]
        sum_without[2] += valuation[j][r]
    elif v == 'C':
        sum_without[0] += valuation[j][r]
        sum_without[1] += valuation[j][r]


print('VCG player1 pay:', max_without[0]-sum_without[0])
print('VCG player2 pay:', max_without[1]-sum_without[1])
print('VCG player3 pay:', max_without[2]-sum_without[2])