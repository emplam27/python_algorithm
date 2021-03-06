"""
         19 20 21
         22 23 24
         25 26 27
10 11 12  1  2  3 28 29 30
13 14 15  4  5  6 31 32 33
16 17 18  7  8  9 34 35 36
         37 38 39
         40 41 42
         43 44 45
         46 47 48
         49 50 51
         52 53 54

반시계방향은 시계 방향을 3번 돌리도록 하자
"""

import sys

sys.stdin = open('input.txt', 'r')

rotates = [
    {1: 7, 2: 4, 3: 1, 4: 8, 6: 2, 7: 9, 8: 6, 9: 3, 12: 37, 15: 38, 18: 39, 37: 34, 38: 31, 39: 28, 34: 27, 31: 26,
     28: 25, 27: 12, 26: 15, 25: 18},  # 윗면 시계방향
    {46: 52, 47: 49, 48: 46, 49: 53, 51: 47, 52: 54, 53: 51, 54: 48, 43: 10, 44: 13, 45: 16, 10: 21, 13: 20, 16: 19,
     19: 30, 20: 33, 21: 36, 30: 45, 33: 44, 36: 43},  # 아랫면 시계방향
    {37: 43, 38: 40, 39: 37, 40: 44, 42: 38, 43: 45, 44: 42, 45: 39, 7: 16, 8: 17, 9: 18, 16: 48, 17: 47, 18: 46,
     46: 36, 47: 35, 48: 34, 34: 7, 35: 8, 36: 9},  # 앞 면 시계방향
    {19: 25, 20: 22, 21: 19, 22: 26, 24: 20, 25: 27, 26: 24, 27: 21, 1: 28, 2: 29, 3: 30, 28: 54, 29: 53, 30: 52,
     52: 12, 53: 11, 54: 10, 12: 3, 11: 2, 10: 1},  # 뒷면 시계방향
    {10: 16, 11: 13, 12: 10, 13: 17, 15: 11, 16: 18, 17: 15, 18: 12, 1: 19, 4: 22, 7: 25, 19: 46, 22: 49, 25: 52,
     46: 37, 49: 40, 52: 43, 37: 1, 40: 4, 43: 7},  # 왼쪽 면 시계방향
    {28: 34, 29: 31, 30: 28, 31: 35, 33: 29, 34: 36, 35: 33, 36: 30, 3: 39, 6: 42, 9: 45, 39: 48, 42: 51, 45: 54,
     48: 21, 51: 24, 54: 27, 21: 3, 24: 6, 27: 9},  # 오른쪽 면 시계방향
]

T = int(input())
for _ in range(T):
    N = int(input())
    orders = list(input().split())
    cube = [0] + ['w'] * 9 + ['g'] * 9 + ['o'] * 9 + ['b'] * 9 + ['r'] * 9 + ['y'] * 9
    for order in orders:
        prev_cude = cube[:]

        # 움직일 면 결정
        if order[0] == 'U': index = 0
        elif order[0] == 'D': index = 1
        elif order[0] == 'F': index = 2
        elif order[0] == 'B': index = 3
        elif order[0] == 'L': index = 4
        else: index = 5

        # 방향 결정
        if order[1] == '+': direction = 1
        else: direction = 3

        for _ in range(direction):
            for key, value in rotates[index].items():
                cube[key] = prev_cude[value]
            prev_cude = cube[:]

    tmp_print = ''
    for i, j in enumerate(cube[1:10]):
        tmp_print += j
        if i % 3 == 2:
            print(tmp_print)
            tmp_print = ''