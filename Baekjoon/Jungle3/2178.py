from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

# print(graph)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque([[x, y]])
    # queue.append([x,y])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny)
            if not (nx < 0 or ny < 0 or nx > N-1 or ny > M-1 or graph[x][y] == 0):
                if graph[nx][ny] == 1:
                    # print(graph[nx][ny], graph[x][y])
                    graph[nx][ny] = graph[x][y] + 1
                    # graph[nx][ny] = graph[x][y] - 1
                    queue.append((nx, ny))

                    # ⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂ 진행 상황 쉽게 알아보기 ⁂⁂⁂⁂⁂⁂⁂⁂⁂⁂
                    # for k in range(N):
                    #     print(graph[k])
                    # print()

    # return graph[N-1][M-1]


def bfs1(queue):
    queue = [[0, 0]]

    while queue:
        x, y = queue[0][0], queue[0][1]

        del queue[0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and ny >= 0 and nx < N and ny < M:
                if graph[nx][ny] == "1":
                    queue.append([nx, ny])
                    graph[nx][ny] = graph[x][y] + 1

bfs(0, 0)
# print(bfs(0, 0))

# queue = []
# bfs1(queue)
print(graph[N-1][M-1])










# import sys
# input=sys.stdin.readline

# N, M = map(int, input().split()) # 배열크기 NXM

# graph = [] # 배열

# #배열 입력
# for _ in range(N) :
#     graph.append(list(input()))

# #배열을 int형으로 선언
# graph[0][0] = 1

# #상하좌우
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# queue = [[0,0]] #시작 좌표

# #BFS 시작
# while queue :
#     x, y = queue[0][0], queue[0][1]

#     del queue[0]

#     for i in range(4) :
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if nx>=0 and ny>=0 and nx<N and ny<M :
#             if graph[nx][ny]=="1" :
#                 queue.append([nx,ny])
#                 graph[nx][ny] = graph[x][y] + 1

# print(graph[N-1][M-1])
