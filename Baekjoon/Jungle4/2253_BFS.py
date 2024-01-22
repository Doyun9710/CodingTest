# BFS
from collections import deque

N, M = list(map(int, input().split()))
dp = [0] * (N+1)
for _ in range(M):
    small = int(input())
    dp[small] = -1

dp[1] = 0
dp[2] = 1

queue = deque()
queue.append([1, 2, 1])
aaaaa = 0
# cnt = 1
add = [[0] * N for _ in range(N)]
# for i in range(N):
while queue:
    time, now, speed = queue.popleft()
    # queue.append([now, speed])
    # print(now, speed, queue)

    for jump in [speed-1, speed, speed+1]:
        next = now + jump
        # print(next, jump)
        if next == N:
            aaaaa = 1
            print(time+1)
            break
        if now < next < N and dp[next] == 0 and jump not in add:
            dp[next] = time
            # if next == N:
            #     # print(dp[N])
            #     break
            queue.append([time+1, next, jump])
            add[next].append(jump)
    if aaaaa == 1:
        # print(time+1)
        break

    # if dp[N] != 0:
    #     if aaaaa == 1:
    #         print(time)
    #     elif aaaaa == -1:
    #         print(-1)

# print(dp[N]+1)
# print(aaaaa)
if aaaaa == 0:
    print('-1')