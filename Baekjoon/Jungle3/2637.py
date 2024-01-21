from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
degree = [0] * (N+1)
cost = [[0] * (N+1) for _ in range(N+1)]

# 기본 부품에서 완성본까지 올라가기! 기본부품에서!! 시작!!!
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append([X, K])
    degree[X] += 1


def Topological_Sorting():
    # p1, p2, p3, p4 = 0

    queue = deque([])

    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            cost[i][i] = 1

    # -------------------- graph 와 cost 출력
    # for i in range(1, N+1):
    #     print(i, graph[i], cost[i])

    while queue:
        now = queue.popleft()
        for i, j in graph[now]:
            if graph[i] == None:
                cost[now][i] += j
            else:
                for k in range(1, N+1):
                    cost[i][k] += cost[now][k] * j
            degree[i] -= 1
            if degree[i] == 0:
                queue.append(i)

    for i in range(N+1):
        if cost[N][i] != 0:
            print(i, cost[N][i])


Topological_Sorting()