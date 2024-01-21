import sys
sys.setrecursionlimit(10**6)

def dfs(i, color):
    global answer

    visit[i] = color

    for j in graph[i]:
        # if visit[j] == visit[i]:
        #     answer = False
        #     return
        # else:
        #     visit[i] = color
        #     dfs(j, -color)
        if visit[j] == 0:
            dfs(j, -color)
        elif visit[i] == visit[j]:
            answer = False
            return


K = int(sys.stdin.readline())

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    visit = [0 for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)

    answer = True
    color = 1

    for i in range(1, V+1):
        if not answer:
                break
        if visit[i] == 0:
            dfs(i, color)

    print("YES" if answer else "NO")