# 일곱 난쟁이
import sys
# 퀵 정렬 (오름차순)
# 순열 (노가다?)
n = 9
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))

def sort(arr, l, r):
    i = l
    for j in range(l, r):
        if arr[j] <= arr[r]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def arrsort(arr, l, r):
    if l < r:
        p = sort(arr, l, r)

        arrsort(arr, l, p-1)
        arrsort(arr, p+1, r)

def delnum(arr):
    for i in range(9):
        arr1 = arr[:]
        del arr1[i]
        for j in range(8):
            a = 0
            arr2 = arr1[:]
            del arr2[j]
            # print(arr2)
            for k in range(7):
                a += arr2[k]
            if a == 100:
                return arr2

arrsort(arr, 0, n-1)
answer = delnum(arr)
for i in range(len(answer)):
    print(answer[i])
