from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] * (N+1) for _ in range(N+1)]
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

# ------------------------------------- graph 출력
# for i in range(1, N+1):
#     print(i, graph[i])
# ------------------------------------- graph 출력

start, end = map(int, input().split())
visited = [int(1e9)] * (N+1)


# 선입선출 큐 사용 BFS ( 시간초과 )
def my_bfs_Dijkstra(start):
    queue = []
    queue.append(start)
    visited[start] = 0

    while queue:
        now = queue.pop(0)
        for i, j in graph[now]:
            if (visited[now]+j) < visited[i]:
                visited[i] = visited[now] + j
                queue.append(i)

    print(visited[end])

'''
우선순위 큐를 사용하지 않는 코드에서는, 특정 정점을 기준으로 모든 정점들을 탐색하면서 최소 거리를 찾아야 한다.

이 경우, 정점이 100만개라면 100만*100만 번의 탐색이 필요 (즉, O(V^2))

하지만 우선순위 큐를 사용하면 항상 맨 앞에 최솟값이 들어가도록 유지 가능
그러므로, 큐의 pop 연산만으로도 최소 거리에 있는 정점을 한번에 선택 가능
이 경우, 시간복잡도는 O(ElogV)
(단, 간선의 갯수가 매우 많은 경우에는 O(V^2) 형태의 시간복잡도가 더 효율적일 수도 있다.)
'''

# 최소 Heap 사용 BFS
def bfs_Dijkstra(start):
    heap = []
    
    heappush(heap, (0, start))
    visited[start] = 0
    
    while heap:
        # 가장 최단거리가 짧은 노드에 대한 정보 꺼내기
        distance, now = heappop(heap)

        # 이미 처리된 노드 무시
        # 최단거리테이블을 이용해 방문여부 확인
        if visited[now] < distance:
            continue
        

        for i in graph[now]:
            # cost += i[1] 은 반복 중첩되기 때문에 에러!!
            cost = distance + i[1]

            # 선택된 노드를 거쳐서 이동하는 것이 더 빠른 경우
            if cost < visited[i[0]]:
                # print(heap, '-----------', cost, distance, now, i)
                # print(visited)
                visited[i[0]] = cost
                heappush(heap, (cost, i[0]))
    
    # print(visited)
    print(visited[end])


bfs_Dijkstra(start)




















