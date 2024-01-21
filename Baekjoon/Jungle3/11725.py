import sys
# 런타임 에러 방지
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
# 메모리 초과. 100,000 X 100,000 = 10억
# graph = [[0]*(N+1) for _ in range(N+1)]
# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     graph[x][y] = graph[y][x] = 1

graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# for x in range(N):
#     print(graph[x])
visit_dfs = [0] * (N+1)

# print(graph) 출력 후, 선 그려보기!!
def dfs(parent):
    for child in graph[parent]:
        if visit_dfs[child] == 0:
            visit_dfs[child] = parent
            dfs(child)

dfs(1)

for x in range(2, N+1):
    print(visit_dfs[x])