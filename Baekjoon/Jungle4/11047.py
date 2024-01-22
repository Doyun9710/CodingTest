import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []

for i in range(N):
    coin = int(input())
    coins.append(coin)

coins.sort(reverse=True)

cnt = 0
for i in coins:
    if i <= K:
        while i <= K:
            K -= i
            cnt += 1

print(cnt)





# 속도 빠름
# N, K = map(int, input().split())
# coins=[]
# for i in range(N):
#     coins.append(int(input()))
# coins.sort(reverse=True)

# result=0
# for i in coins:
#     if K==0: 
#       break
#     result += K//i
#     K %= i

# print(result)