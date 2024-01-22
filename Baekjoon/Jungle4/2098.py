# 외판원 순환
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# for i in range(N):
#     for j in range(N):
#         print(graph[i][j], end='  ')
#     print()

dp = [1e9] * (N+1)

def dfs():
    pass

dfs()

print()