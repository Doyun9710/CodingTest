# 예제 4-1 상하좌우

import sys
input = sys.stdin.readline

N = int(input())
movelist = list(map(str, input().split()))

x, y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for i in movelist:
    for j in range(len(move_types)):
        if i == move_types[j]:
            nx = x + dx[j]
            ny = y + dy[j]

    if nx < 1 or ny < 1 or nx > N or ny > N:
        continue

    x, y = nx, ny

print(x, y)



''' input
5
R R R U D D
'''
