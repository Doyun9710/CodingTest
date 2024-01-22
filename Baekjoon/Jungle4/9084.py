import sys
input = sys.stdin.readline

MAX = 10001

T = int(input())

for _ in range(T):
    dp = [0] * MAX
    coin = []

    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    # queue 사용 시 시간, 공간 초과
    # queue = deque(coin)
    # while queue:
    #     now = queue.popleft()
    #     print('now', queue, now)

    #     for next in coin:
    #         now += next
    #         if now < MAX:
    #             dp[now] += 1
    #             queue.append(now)

    dp[0] = 1

    for c in coin:
        for num in range(M+1):
            if num >= c:
                dp[num] += dp[num - c]
    
    # print('answer', dp[M])
    print(dp[M])