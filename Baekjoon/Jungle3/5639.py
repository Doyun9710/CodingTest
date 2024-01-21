import sys
sys.setrecursionlimit(10 ** 9)


# dfs 탐색
def dfs(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return
    temp = end + 1

    # 서브 트리 찾기
    # 처음으로 큰 값이 나오는데 찾는데 시간복잡도 O(n)
    for i in range(start + 1, end + 1): # i의 범위는 배열[1] 부터 [len(list)-1] 까지
        # 루트 보다 크면 오른쪽 서브 트리 ( 98, 52, 60 )
        if graph[start] < graph[i]:
            temp = i
            break

    # 두개로 나눠서 계속 호출하기 때문에 시간복잡도 O(logn)
    # print(start, end, temp)
    dfs(start + 1, temp - 1) # 왼쪽 서브 트리 재귀적으로 탐색
    # print(start, end, temp)
    dfs(temp, end) # 오른쪽 서브 트리 재귀적으로 탐색

    # 결과적으로 nlogn의 시간복잡도를 가지고 시간문제를 통과 할 수 있습니다.
    # print(start, end, temp) # 출력 상황 start, end, temp 출력
    print(graph[start])


# 입력이 없을때까지 반복하여 입력을 리스트에 추가한다.
graph = []
while True:
    try:
        graph.append(int(sys.stdin.readline()))
    except:
        break

dfs(0, len(graph) - 1)


# case 1
# import sys
# sys.setrecursionlimit(10 ** 6)


# def postorder(start, end):
#     if start >= end:
#         return
#     root = preorder[start]

#     if preorder[end - 1] <= root:
#         postorder(start + 1, end)
#         print(root)
#         return

#     idx = 0
#     for i in range(start + 1, end):
#         if preorder[i] > root:
#             idx = i
#             break
#     postorder(start + 1, idx)
#     postorder(idx, end)
#     print(root)


# preorder = []

# while True:
#     try:
#         preorder.append(int(sys.stdin.readline()))
#     except:
#         break

# postorder(0, len(preorder))