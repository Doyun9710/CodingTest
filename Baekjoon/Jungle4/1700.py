# 멀티탭 스케줄링
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
object = list(map(int, input().split()))
# cntlist = [0, 0] * (N+1)
cntlist = [0] * (K+1)

answer = 0

for obj in object:
    cntlist[obj] += 1
#     cntlist[obj]
# cntlist.sort()

# for i in range(K):


print(cntlist)

print(answer)