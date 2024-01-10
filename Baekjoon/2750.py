import sys
# 퀵 정렬
n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(int(sys.stdin.readline()))
# print(arr[:3]) # 처음 원소 3개
arrlen = len(arr)

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

arrsort(arr, 0, arrlen-1)
for i in range(len(arr)):
        print(arr[i])



# RecursionError
# RecursionError는 재귀와 관련된 에러입니다. 가장 많이 발생하는 이유는 Python이 정한 최대 재귀 깊이보다 재귀의 깊이가 더 깊어질 때입니다.
# Python이 정한 최대 재귀 깊이는 sys.getrecursionlimit()을 이용해 확인할 수 있습니다. BOJ의 채점 서버에서 이 값은 1,000으로 되어 있습니다.
# n = int(sys.stdin.readline())
# arr = []

# for i in range(n):
#     a = int(sys.stdin.readline())
#     arr.append(a)

# arrlen = len(arr)

# def arrsort(arr, arrlen):
#     if arrlen == 0:
#         for i in range(len(arr)):
#             print(arr[i])
#         return
#     for i in range(arrlen):
#         a = arr[i]
#         if arr[i] > arr[i+1]:
#             arr[i] = arr[i+1]
#             arr[i+1] = a
#     # print(arr)
#     arrsort(arr, arrlen-1)

# arrsort(arr, arrlen-1)