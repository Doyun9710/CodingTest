import sys

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
    
    if l < pr: sortnumlist(arr, l, pr)
    if pl < r: sortnumlist(arr, pl, r)

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

sortnumlist(arr, 0, len(arr)-1)

for i in range(len(arr)):
        print(arr[i])