import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))

# MAX = float('inf')
MAX = 1e9
Length = int((2 * N)**0.5) # 등차수열?
Length = N # 메모리 초과

# dp = [[MAX] * (int((2 * N)**0.5) + 2) for _ in range(N + 1)]
dp = [[MAX] * (Length + 2) for _ in range(N + 1)]

dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))

for i in range(2, N + 1):
    if i in stone_set:
        continue
    for j in range(1, Length + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == MAX:
    print(-1)
else:
    print(min(dp[N]))



'''
Input
8 2
3
6

Output
5
'''
'''
Input
3 1
2

[정답]
-1
'''
