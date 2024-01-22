# 숫자 카드 게임

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = 0

for i in range(N):
    nlist = list(map(int, input().split()))
    minnum = min(nlist)
    result = max(result, minnum)

print(result)



''' input
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
'''