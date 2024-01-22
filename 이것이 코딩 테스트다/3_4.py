# 1이 될 때까지

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
cnt = 0

while(N != 1):
    if (N % K == 0):
        N = N // K
    else:
        N -= 1

    cnt += 1

print(cnt)


''' input
25 5
27 5
'''