from collections import deque
import sys
input = sys.stdin.readline
# https://resilient-923.tistory.com/263
M, N, H = map(int, input().split())
Box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
queue = deque()

# 높이, x, y 순서 (H, N, M)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if Box[i][j][k] == 1:
                queue.append((i,j,k))

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

for i in range(H):
    print()
    for j in range(N):
        print(Box[i][j])

def bfs():
    
    pass

bfs()