from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] * (N+1) for _ in range(N+1)]
in_degree = [0] * (N+1)
visited = [False] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

# print(graph)
# print(in_degree)


def Topological_Sorting():
    queue = deque()

    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
            visited[i] = True

    # print(queue)

    while queue:
        
        num = queue.popleft()
        print(num, end=' ')

        for i in graph[num]:
            if in_degree[i] == 1:
                queue.append(i)
                visited[i] = True
            else:
                in_degree[i] -= 1


Topological_Sorting()
