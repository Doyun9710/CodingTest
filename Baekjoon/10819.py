# # 차이를 최대로
# 공식이 없는가? 노가다 뿐인가?
import sys, itertools

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_num = 0
for c in itertools.permutations(arr,N):
    tmp = 0
    for i in range(N-1):
        tmp += abs(c[i] - c[i+1])
        print(c[i], c[i+1])
    
    max_num = max(max_num, tmp)
print(max_num)










# chars = ['A', 'B', 'C']

# p = itertools.permutations(chars, 2)  # 순열
# c = itertools.combinations(chars, 2)  # 조합
# print(list(p))      # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# print(list(c))      # [('A', 'B'), ('A', 'C'), ('B', 'C')]





# import sys

# def sortnumlist(arr, l: int, r: int):
#     pl = l
#     pr = r
#     p = arr[(l+r)//2]
#     # print(p)
#     while pl <= pr:
#         while arr[pl] < p:
#             pl += 1
#         while p < arr[pr]:
#             pr -= 1
#         if pl <= pr:
#             arr[pl], arr[pr] = arr[pr], arr[pl]
#             pl += 1
#             pr -= 1
    
#     if l < pr: sortnumlist(arr, l, pr)
#     if pl < r: sortnumlist(arr, pl, r)

# n = int(sys.stdin.readline())
# listnum = list(map(int, sys.stdin.readline().split()))
# answer = [None] * len(listnum)

# sortnumlist(listnum, 0, len(listnum)-1)
# print(listnum)

# for i in range(0, len(listnum), 2):
#     # print(i)
#     answer[i], answer[i+1] = listnum[i], listnum[len(listnum)-1-i]
# print(answer)
# ans = 0
# for j in range(0, len(answer), 2):
#     ans += abs(answer[i]-answer[i+1])
# print(ans)