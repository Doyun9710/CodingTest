import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    newbie = []
    for _ in range(N):
        documents, interview = map(int, input().split())
        newbie.append([documents, interview])
    newbie.sort()

    # print(newbie)

    checkpoint = N + 1
    cnt = 0

    for i, j in newbie:
        if j < checkpoint:
            cnt += 1
            checkpoint = j

    print(cnt)