# 예제 4-1 상하좌우

import sys
input = sys.stdin.readline

N = input()
movelist = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_type = ['L', 'R', 'U', 'D']

for i in movelist:
    # print(i)
    pass




''' input
5
R R R U D D
'''