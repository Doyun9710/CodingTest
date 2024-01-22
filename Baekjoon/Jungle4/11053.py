import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N)

# for num in arr:
#     cnt = 0
#     for i in range(N-1):
#         if check[i] < check[i+1]:
#             pass

for i in range(N):
    for j in range(i):
        print('now', arr[i], arr, dp)
        if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
            print('next', arr, dp, end='\n\n')
    dp[i] += 1

print(max(dp))