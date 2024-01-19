import sys
# 문제 이해를 잘 못하겠음;;

def sortnumlist(arr, l, r):
    pl = l
    pr = r
    p = arr[(l+r)//2]
    while pl <= pr:
        while arr[pl] < p:
            pl += 1
        while p < arr[pr]:
            pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

    if l < pr:
        sortnumlist(arr, l, pr)
    if pl < r:
        sortnumlist(arr, pl, r)


def binary_search(xlist, start, end):
    while start <= end:
        mid = (start + end) // 2
        current = xlist[0]
        count = 1

        for i in range(1, len(xlist)):
            if xlist[i] >= current + mid:
                count += 1
                current = xlist[i]

        if count >= c:
            global answer
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


n, c = list(map(int, sys.stdin.readline().split()))
xlist = []
for _ in range(n):
    xlist.append(int(sys.stdin.readline()))

# 정렬
sortnumlist(xlist, 0, len(xlist)-1)

start = 1
end = xlist[-1] - xlist[0]
answer = 0

binary_search(xlist, start, end)
print(answer)