import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
days = 0
lst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            lst.append((arr[i][j], i, j, days))

lst.sort()

q = deque(lst)
# for virus_num, pos_x, pos_y, day in lst:
#     q.append((virus_num, pos_x, pos_y, day))

S, X, Y = map(int, input().split())

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    # 번호가 낮은 바이러스가 순서대로 자리 차지함
    global arr
    
    while q:
        virus_num, x, y, day = q.popleft()

        if S == day:
            # print(arr)
            # return arr[X-1][Y-1]
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 아직 바이러스가 자리 차지를 하지 않았다면
                if arr[nx][ny] == 0:
                    arr[nx][ny] = virus_num
                    q.append((arr[nx][ny], nx, ny, (day + 1)))
    return arr[X-1][Y-1]

print(bfs())
# bfs()
# print(arr[X-1][Y-1])