import sys
input = sys.stdin.readline


'''

# 1. 단순 무게 순 정렬. 틀림
# for _ in range(N):
#     object.append(list(map(int, input().split())))
# object.sort()


# 2-1. 중요도(v/w -> 무게당 가치) 우선 정렬. 틀림
for _ in range(N):
    w, v = map(int, input().split())
    if w < K and v != 0:
        importance = v / w
        object.append([importance, w, v])
# object.sort(key = lambda x:-x[0])

# 2-2. 1순위 중요도, 2순위 무게 / 가치 정렬. 틀림
object.sort(key = lambda x:(-x[0], x[1]))
object.sort(key = lambda x:(-x[0], -x[2]))


sumW = 0
sumV = 0
for w, v in object:
    if (sumW + w) <= K:
        sumW += w
        sumV += v

'''


N, K = map(int, input().split())
object = [[0, 0]]
for _ in range(N):
    object.append(list(map(int, input().split())))
# object.sort()
# print(object)

dp = [[0] * (K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        weight, value = object[i]

        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - weight] + value)

        # print(dp)
print(dp[N][K])