from collections import deque
import sys
input = sys.stdin.readline
# 왜 에러???

def bfs(x):
    global city

    queue = deque([x])
    visited[x] = 0

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[x] + 1
                if visited[i] == K:
                    city.append(i)
                    
        # print('-------------', queue, '-------------', city)


N, M, K, X = map(int, input().split())
visited = [0] * (N+1)

# graph = [[0] * (N+1) for _ in range(N+1)]
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)
# print(graph, visited)

city = []
bfs(X)

# if len(city) == 0:
#     print('-1')
# else:
#     city.sort()
#     for i in city:
#         print(i)

# K값이 distance에 있다면 i값출력 없다면 -1 출력
if K in visited:
  for i in range(1, N+1):
    if visited[i] == K:
      print(i)
    #   check = True
else:
    print(-1)










# from collections import deque
# import sys
# f = sys.stdin.readline

# n, m, k, x = map(int, f().split())
# graph = [[] for _ in range(n+1)]
# distance = [0] * (n+1)
# visited = [False] * (n+1)

# for _ in range(m):
#     a, b = map(int, f().split())
#     graph[a].append(b)

# def bfs(start):
#     answer = []
#     q = deque([start])
#     visited[start] = True
#     distance[start] = 0
#     while q:
#         now = q.popleft()
#         for i in graph[now]:
#             if not visited[i]:
#                 visited[i] = True
#                 q.append(i)
#                 distance[i] = distance[now] + 1
#                 if distance[i] == k:
#                     answer.append(i)
#     if len(answer) == 0:
#         print(-1)
#     else:
#         answer.sort()
#         for i in answer:
#             print(i, end='\n')

# bfs(x)