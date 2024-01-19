import sys

n, m = map(int, sys.stdin.readline().split())
numlist = list(map(int, sys.stdin.readline().split()))

# 최대값 구하기
# num_max = numlist[0]
# for i in range(len(numlist)-1):
#     if num_max < numlist[i+1]:
#         num_max = numlist[i+1]
num_min, num_max = 0, max(numlist)

while num_min <= num_max:
    mid = (num_min + num_max)//2
    s = 0
    for i in numlist:
        if i > mid:
            s += i - mid
    if s < m:
        num_max = mid - 1
    else:
        num_min = mid + 1

print(num_max)