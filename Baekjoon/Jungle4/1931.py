import sys
input = sys.stdin.readline

N = int(input())

timelist = []

for _ in range(N):
    timelist.append(list(map(int, input().split())))
timelist.sort(key=lambda x: (x[1], x[0]))


# for i in range(len(timelist)):
#     if (len(timelist) - i) < MAX:
#         break
#     point = 0
#     cnt = 0
#     for s, e in timelist[i:]:
#         if point <= s:
#             # print('s, e : ', s, e)
#             point = e
#             cnt += 1
#     if MAX < cnt:
#         MAX = cnt


MAX = 0
point = 0
cnt = 0

for s, e in timelist:
    if point <= s:
        point = e
        cnt += 1
    if MAX < cnt:
        MAX = cnt

print(MAX)
