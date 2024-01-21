import sys

N, M, V = list(map(int, sys.stdin.readline().split()))
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x][y] = graph[y][x] = 1

visit_dfs = [0] * (N+1)
visit_bfs = [0] * (N+1)

# print(N, M, V, graph)

def dfs(V):
    print(V, end=' ')
    visit_dfs[V] = 1
    for i in range(1, N+1):
        if graph[V][i] == 1 and visit_dfs[i] == 0:
            dfs(i)

def bfs(V):
    queue = [V]
    visit_bfs[V] = 1
    while queue:
        # visit_bfs[V] = 1
        V = queue.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if graph[V][i] == 1 and visit_bfs[i] == 0:
                queue.append(i)
                visit_bfs[i] = 1

dfs(V)
print()
bfs(V)