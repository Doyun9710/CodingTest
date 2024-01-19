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

    if l < pr:
        sortnumlist(arr, l, pr)
    if pl < r:
        sortnumlist(arr, pl, r)


def find_col(numlist):
    startnum = 0
    endnum = len(numlist) - 1
    
    global min
    while startnum < endnum:
        
        sumnum = numlist[startnum] + numlist[endnum]

        if sumnum == 0:
            answer = numlist[startnum], numlist[endnum]
            break
        
        if abs(sumnum) < min:
            min = abs(sumnum)
            answer = numlist[startnum], numlist[endnum]
        if sumnum > 0:
            endnum -= 1
        else:
            startnum += 1
    for i in sorted(answer):
        print(i, end=' ')

N = int(sys.stdin.readline())
list_A = list(map(int, sys.stdin.readline().split()))
min = max(list_A)
# 순서 정렬
sortnumlist(list_A, 0, len(list_A)-1)
# 높이 자르기, 비교
find_col(list_A)

# import sys
# input = sys.stdin.readline

# N = int(input())
# arr = sorted(list(map(int, input().split())))

# start = 0
# end = len(arr)-1

# min = sys.maxsize
# while start < end:
#     calc = arr[start] + arr[end]
#     if abs(calc) < min:
#         min = abs(calc)
#         answer = arr[start], arr[end]
#     if calc == 0:
#         break
#     if calc < 0:
#         start += 1
#     else:
#         end -= 1

# for i in sorted(answer):
#     print(i, end=' ')