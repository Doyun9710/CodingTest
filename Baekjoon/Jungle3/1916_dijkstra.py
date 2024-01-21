import sys
from heapq import heappush, heappop

input = sys.stdin.readline # 빠른 입력
INF = int(1e9)              # 무한을 의미하는 값으로 10억 설정

N = int(input())            # 노드의 개수
M = int(input())            # 간선의 개수를 입력받기
distance = [INF]*(N+1)      # 최단거리 테이블(각 정점사이의 거리 무한대로 초기화)

# 노드 연결정보
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    # a번노드에서 b번 노드로 가는 비용c
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
# print(graph)

# 출발 노드와 도착 노드 번호를 입력받기
start, end = map(int, input().split())

# 다익스트라 알고리즘(최소힙 이용))
def dijkstra(start):
    heap = []
    # 시작 노드
    heappush(heap, (0, start))
    distance[start] = 0  # 시작 지점 0으로 초기화
    
    while heap:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(heap)
        # 이미 처리된 노드였다면 무시
        # 별도의 visited 테이블이 필요없이, 최단거리테이블을 이용해 방문여부 확인
        if distance[now] < dist:
            continue
        # 선택된 노드와 인접한 노드를 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(heap, (cost, i[0]))


# 다익스트라 알고리즘수행
dijkstra(start)

# 도착 노드로 가기 위한 최단 거리를 출력
print(distance[end])